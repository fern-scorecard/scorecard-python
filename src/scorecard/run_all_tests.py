import os 
import typing

from .core import ApiError
from .client import Scorecard


def run_all_tests(
    *,
    input_testset_id: int,
    scoring_config_id: int,
    model_invocation: typing.Callable[[str], typing.Any],
    api_key: typing.Optional[str] = os.getenv("SCORECARD_API_KEY")
) -> None: 
    """
    Runs all tests within a testset.

    Parameters:
        - input_testset_id: int. The ID of the Test Set you want to run.

        - scoring_config_id: int. 

        - model_invocation: typing.Callable[[typing.str], typing.Any].
          A function that will call your AI model with a prompt.

        - api_key: typing.Optional[str]. 
          Your Scorecard API Key. Defaults to SCORECARD_API_KEY.
    """
    if api_key is None: 
        raise ApiError(body="Please provide api_key or add SCORECARD_API_KEY to your environment")
    client = Scorecard(api_key=api_key)
    run_id = client.run.create(
        testset_id=input_testset_id, 
        scoring_config_id=scoring_config_id
    )
    testcases = client.testset.get(input_testset_id)

    for testcase in testcases:
        testcase_id = testcase['id']
        query = testcase['user_query']

        print(f"Running testcase {testcase_id}...")
        print(f"User query: {query}")

        response = model_invocation(query)

        client.testrecord.create(
            run_id=run_id,
            testcase_id=testcase_id,
            model_response=response,
        )

    print("Finished running testcases...")

