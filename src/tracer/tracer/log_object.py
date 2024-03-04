from datetime import datetime, timedelta
from inspect import BoundArguments, Signature, _empty
from typing import Any, List, Union, Dict

from openai._types import NotGiven
from pydantic import (BaseModel, Field, FieldSerializationInfo,
                      SerializerFunctionWrapHandler, computed_field,
                      field_serializer)


def type_to_str(t: Any) -> str:
    """
    Converts a type to a human-readable string.
    Handles basic types, typing module generics, and custom types.
    """
    # Handle typing module generics
    if hasattr(t, '__origin__'):
        # Special handling for Union types
        if t.__origin__ is Union:
            return f"Union[{', '.join(type_to_str(arg) for arg in t.__args__)}]"
        elif hasattr(t, '__args__'):
            return f"{t.__origin__.__name__}[{', '.join(type_to_str(arg) for arg in t.__args__)}]"
    # Basic and custom types
    return t.__name__ if hasattr(t, '__name__') else str(t)


class InputArgument(BaseModel):
    label: str
    type: str
    value: Any = Field(default=None)

    @field_serializer('value', when_used='always', mode='wrap')
    def serialize_value(self,
                        value: Any,
                        nxt: SerializerFunctionWrapHandler,
                        info: FieldSerializationInfo
                        ):

        if isinstance(value, NotGiven):
            return 'NotGiven'
        return nxt(value)

    def jsonify(self) -> Dict[str, Any]:
        return {self.label: self.value}


class Input(BaseModel):
    args: list[InputArgument]

    @classmethod
    def from_bound_arguments(cls, args: BoundArguments,
                             sig: Signature) -> 'Input':
        res = []

        for name, value in args.arguments.items():

            arg_type = type_to_str(sig.parameters[name].annotation)
            input_argument = InputArgument(
                label=name, type=arg_type, value=value)
            res.append(input_argument)

        return cls(args=res)

    def jsonify(self) -> Dict[str, Any]:
        return {k:v for arg in self.args for k,v in arg.jsonify().items()}


class Output(BaseModel):
    type: str
    value: Any

    @classmethod
    def from_return_value(cls, value: Any, sig: Signature) -> 'Output':
        return cls(type=type_to_str(sig.return_annotation), value=value)
