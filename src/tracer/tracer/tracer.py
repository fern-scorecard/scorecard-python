import functools
from types import TracebackType
import uuid
from contextvars import ContextVar
from datetime import datetime
from inspect import BoundArguments, Signature, _empty, signature
from typing import Any, Callable, Dict, List, Tuple
from tracer.database import LogRecord, Session, TestSet, TestCase

from tracer.log_object import Input, Output
from tracer.pusher import LogPusher

current_trace_id:ContextVar[str] = ContextVar('current_trace_id', default='')
current_span_id:ContextVar[str] = ContextVar('current_span_id', default='')
current_session_id: ContextVar[int] = ContextVar('current_session', default=-1)
sessions: ContextVar[Dict[int, 'ScorecardSessionManager']] = ContextVar('sessions', default={})
is_run_context: ContextVar[bool] = ContextVar('is_run_context', default=False)

class RunContextManager:
    def __init__(self, test_set: TestSet | int, runnable: Callable[..., Any] | None = None) -> None:
        if isinstance(test_set, int):
            test_set = TestSet.get(test_set)
        self.test_set: TestSet = test_set
        self.test_cases: List[TestCase] = test_set.get_test_cases()
        self._index: int = 0
        self.runnable = scorecard_function_tracer(runnable) if runnable else None
        self.session = Session(tags={"type": "test_run", "source_test_set": str(self.test_set.id)}).insert()

        if not self.session.id:
            raise ValueError('Session failed to save.')

        current_session_id.set(self.session.id)

        is_run_context.set(True)
        
    
    def __enter__(self) -> 'RunContextManager':
        return self
    
    def __exit__(self, exc_type: type | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        pass
    
    def __iter__(self) -> 'RunContextManager':
        self._index = 0  # Reset the index each time iter is called
        return self

    def __next__(self) -> Dict[str, Any]:
        if self._index < len(self.test_cases):
            result = self.test_cases[self._index]
            self._index += 1
            return result.input.jsonify()
        else:
            raise StopIteration
    
    def run(self):
        if self.runnable:
            for input in self:
                try:
                    print(input)
                    self.runnable(**input)
                except Exception as e:
                    raise ValueError("The supplied test case does not match the given function") from e
        else:
            raise ValueError('You must provide a runnable function if you want to run the test set.')

    

class ScorecardSessionManager:
    def __init__(self, 
                 create_test_set: bool = True, 
                 test_set_prefix: str | None = None,
                 include_intermediates: bool = False, 
                 tags: Dict[str, str] = {}):

        self.session = Session(tags=tags).insert()
        if not self.session.id:
            raise ValueError('Session failed to save.')

        self.create_test_set = create_test_set

        self.test_set_map: Dict[Tuple[str,Signature], TestSet] = {}

        if create_test_set:
            if not test_set_prefix:
                raise ValueError('You must provide a test set name if you want to create a test set.')

        self.test_set_prefix = test_set_prefix
        self.include_intermediates = include_intermediates

        sessions.get()[self.session.id] =  self
    
    @property
    def id(self)->int:
        if not self.session.id:
            raise ValueError('Session has not been saved yet')
        return self.session.id
    
    def add_test_case(self, input: Input, output: Output, function_name: str, signature: Signature, intermediate: bool = False):
        key = (function_name, signature)
        if key not in self.test_set_map.keys():
           test_set = TestSet(name=f"{self.test_set_prefix}#{function_name}#{"intermediate" if intermediate else "root"}", session=self.session.id).insert()
           self.test_set_map[key] = test_set
        
        test_set = self.test_set_map[key]
        test_set.add_test_case(input).record(output)
         
    def __enter__(self) -> 'ScorecardSessionManager':
        if not self.session.id:
            raise ValueError('Session has not been saved yet')
        current_session_id.set(self.session.id)
        return self

    def __exit__(self, exc_type: type | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        pass


def enforce_full_type_annotations(
        func: Callable[..., Any], sig: Signature) -> None:
    for name, param in sig.parameters.items():
        if param.annotation is _empty:
            raise TypeError(
                f"Function '{func.__name__}': Parameter '{name}' lacks a type annotation")
    if sig.return_annotation is _empty:
        raise TypeError(
            f"Function '{func.__name__}': Return type is unannotated")


def type_check(func: Callable[..., Any], args: Tuple,
               kwargs: Dict, sig: Signature) -> BoundArguments:
    bound_arguments = sig.bind(*args, **kwargs)
    bound_arguments.apply_defaults()

    """
    # Leaving this out for later because
    # python does not have great support for
    # instance checking bound generic types.
    # This causes the patch on the openai
    # chat completions to fail.
    # Since this is a nice to have and not required,
    # We can deal with this later.
    for name, value in bound_arguments.arguments.items():
        expected_type = sig.parameters[name].annotation
        if not isinstance(value, expected_type):
            raise TypeError(
                f"Function '{func.__name__}': Argument '{name}' must be of type '{expected_type.__name__}', got '{type(value).__name__}' instead")
    """
    return bound_arguments


def scorecard_function_tracer(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if current_session_id.get() == -1 and not is_run_context.get():
            raise ValueError('No session found. You must use the SessionManager context manager.')

        session_id = current_session_id.get()

        if not is_run_context.get():
            session_manager = sessions.get()[session_id]
        else:
            session_manager = None


        parent_span_id = current_span_id.get()

        if current_trace_id.get() in [None, '']:
            trace_id = str(uuid.uuid4())
            current_trace_id.set(trace_id)
        else:
            trace_id = current_trace_id.get()

        span_id = str(uuid.uuid4())
        current_span_id.set(span_id)

        start_time = datetime.now()

        sig = signature(func)

        enforce_full_type_annotations(func, sig)
        inputs = type_check(func, args, kwargs, sig)

        result = func(*args, **kwargs)

        input = Input.from_bound_arguments(inputs, sig)
        output = Output.from_return_value(result, sig)

        log_object = LogRecord(
            trace_id=trace_id,
            parent_span_id=parent_span_id if parent_span_id != "" else None,
            span_id=span_id,
            function_name=func.__name__,
            start_time=start_time,
            end_time=datetime.now(),
            inputs=input.args,
            output=output,
            session=session_id
            )

        LogPusher(log_object).start()

        current_span_id.set(parent_span_id)
        if parent_span_id == '': # this is a root span
            current_trace_id.set('')
            if not is_run_context.get() and session_manager and session_manager.create_test_set:
                session_manager.add_test_case(input, output, func.__name__, sig)
        else:
            # this is an intermediate span
            if not is_run_context.get() and session_manager and session_manager.create_test_set and session_manager.include_intermediates:
                session_manager.add_test_case(input, output, func.__name__, sig, intermediate=True)
            
            

        return result
    return wrapper