# mypy: ignore-errors
# this file is not a part of the sdk and has only been used
# during development for testing. Committing it as is for now,
# but this file will be removed before the sdk is released.
from openai import OpenAI
from openai.types.chat import ChatCompletion
from pydantic_settings import BaseSettings, SettingsConfigDict

from tracer import RunContextManager, scorecard_function_tracer, scorecard_tracer


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="OPENAI_"
    )

    api_key: str = ""


settings = Settings()


@scorecard_function_tracer
def mult(x: int, y: int) -> int:
    return x * y


@scorecard_function_tracer
def add(a: int, b: int) -> int:
    return a + b


@scorecard_function_tracer
def sum_of_squares(a: int, b: int) -> int:
    return add(mult(a, a), mult(b, b))


@scorecard_function_tracer
def prompt_llm(prompt: str) -> ChatCompletion:
    client = OpenAI(api_key=settings.api_key)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4",
    )

    return response


def prompt_llm_intercept(prompt: str) -> ChatCompletion:
    client = OpenAI(api_key=settings.api_key)
    client = scorecard_tracer(client)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4",
    )
    return response


@scorecard_function_tracer
def call_llm_and_sum_of_squares(a: int, b: int) -> ChatCompletion:

    prompt = f"confirm if the sum of squares of {a} and {b} is {sum_of_squares(a, b)}."
    return prompt_llm(prompt)


# session
if __name__ == "__main__":

    # with ScorecardSessionManager(test_set_prefix="create_live_test_set",
    #                              tags={'type': 'production'},
    #                              create_test_set=True,
    #                             include_intermediates=True
    #                              ) as session:
    #    call_llm_and_sum_of_squares(44, 67)

    # with ScorecardSessionManager(test_set_prefix="live_demo2",
    #                              tags={'type': 'test sessions'},
    #                              create_test_set=True,
    #                              include_intermediates=True) as session:
    #     # Trace 1
    #     call_llm_and_sum_of_squares(7, 8)
    #     # Trace 2
    #     call_llm_and_sum_of_squares(9, 10)

    # Later on
    # test_set = TestSet(id='test_a')
    # with RunContextManager(test_set=11) as run_context:
    #    for test_case in run_context:
    #        print(test_case)

    RunContextManager(test_set=37, runnable=prompt_llm).run()
