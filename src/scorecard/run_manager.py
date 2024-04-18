from typing import Callable, Tuple
from scorecard.client import Scorecard
from scorecard.types import RunStatus, TestCase, Run
from scorecard.api_key import get_api_key
from pydantic import BaseModel


class TestOutput(BaseModel):
    context: str
    response: str

class RunManager:
    def __init__(self, test_set: int, scoring_config_id: int, runnable: Callable[[TestCase], TestOutput], client: Scorecard | None = None):
        self.test_set = test_set
        self.scoring_config_id = scoring_config_id
        self.runnable = runnable
        if client is None:
            self.client = Scorecard(api_key=get_api_key())
        else:
            self.client = client

    def run(self) -> Tuple[Run, str]:
        run = self.client.run.create(testset_id=self.test_set, scoring_config_id=self.scoring_config_id)
        if run.id is None:
            raise ValueError("Failed to create run")

        run = self.client.run.update_status(run_id=run.id, status=RunStatus.RUNNING_EXECUTION)

        if run.id is None: 
            raise ValueError("Failed to update run status to RUNNING_EXECUTION")

        try:
            print("here")
            for testcase in self.client.testset.get_testcases(testset_id=self.test_set).results:
                test_record = self.runnable(testcase)
                self.client.testrecord.create(run_id=run.id,
                                              testset_id=self.test_set,
                                              testcase_id=testcase.id,
                                              user_query=testcase.user_query,
                                              context=test_record.context,
                                              response=test_record.response)
        except Exception as e:
            print(e)
        finally:
            self.client.run.update_status(run_id=run.id, status=RunStatus.AWAITING_SCORING)

            return run , f"https://app.getscorecard.ai/view-records/{run.id}"