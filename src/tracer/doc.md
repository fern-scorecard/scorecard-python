The Scorecard Tracer Module supports the following use cases

# Open AI Call Interception

Calls to Open AI's API can be intercepted and logged by the scorecard_tracer.

```
from tracer import scorecard_function_tracer, ScorecardSessionManager
with ScorecardSessionManager() as session:
    client = OpenAI(api_key=settings.api_key)
    client = scorecard_tracer(client)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4",)
```

All inputs and outputs using the create method of the chat.completions object will be intercepted and logged to scorecard.



# Automatic Logging
You can use the scorecard_function_tracer to automatically log function inputs and outputs during execution. 

```
@scorecard_function_tracer
def multiply(a: int, b: int) -> int:
    return a * b

@scorecard_function_tracer
def add(a: int, b: int) -> int:
    return a + b

with ScorecardSessionManager() as session:
    multiply(add(3,5), 10)

```

This will create a trace that logs the inputs and outputs to the multiply and add functions.
The trace will also contain information about the execution graph.
Any annotated function that is called within the traced function will also be traced.


# Automatic Test Set Creation
You can use the scorecard_function_tracer in conjunction with the scorecard_function_tracer to automatically
create test sets and test cases.

```
@scorecard_function_tracer
def call_llm_and_sum_of_squares(a: int, b: int) -> ChatCompletion:

    prompt = f"confirm if the sum of squares of {a} and {b} is {sum_of_squares(a, b)}."
    return prompt_llm(prompt)

with ScorecardSessionManager(test_set_prefix="create_live_test_set", 
                                 tags={'type': 'production'},
                                  create_test_set=True,) as session:
        for i in range(10):
            for j in range(11, 20):
                call_llm_and_sum_of_squares(i, j)
```

The above will create a single test set with 100 test cases. Each test case will contain the input to the funciton call and the expected output. In addition to this, traces and spans for each function call and annotated sub function calls will be created and logged to scorecard.


# Automatic Test Set Creation with Intermediates
You can use the scorecard_function_tracer in conjunction with the scorecard_function_tracer to automatically
create test sets and test cases. In addition to this, you can also include the intermediates of any annotated function calls in the test set. All of the calls to a single function will be aggregated into a single test set

```
@scorecard_function_tracer
def multiply(a: int, b: int) -> int:
    return a * b

@scorecard_function_tracer
def add(a: int, b: int) -> int:
    return a + b

with ScorecardSessionManager(test_set_prefix="create_live_test_set", 
                                  tags={'type': 'production'},
                                 create_test_set=True,
                                 include_intermediates=True) as session:
    multiply(add(3,5), 10)
```

This will create two test sets. The first is create_list_test_set#add, which will contain the inputs and outputs of the add function. The second is create_list_test_set#multiply, which will contain the inputs and outputs of the multiply function. In addition to this, logs will be emitted for all annotated functions. This is useful for capturing production data for later analysis, or for creating test sets on the fly.


# Test Set Replay

You can use the RunContextManager to replay a test set against a function. This is useful for debugging, or iterating on prompt definitions. All inputs and outputs will be logged as spans and traces which is useful for comparing the changes to the output of prompts as the definitions change.

```
from tracer import RunContextManager

@scorecard_function_tracer
def prompt_llm(prompt: str) -> ChatCompletion:
    return client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4",)

RunContextManager(test_set=37, runnable=prompt_llm).run()
```

This will run all of the test cases in the test_set with Id 37 against the prompt_llm function, and record the inputs and outputs for later analysis.
