from datetime import datetime
import pytest
from unittest.mock import MagicMock, patch
from scorecard.run_manager import RunManager, TestOutput
from scorecard.types import RunStatus, TestCase, Run
from dotenv import load_dotenv, set_key
from os import remove

@pytest.fixture
def run_manager_setup_teardown():
    fake_env_file = '.env.test'
    test_set = 123
    scoring_config_id = 456
    runnable = MagicMock(return_value={'context': 'test_context', 'response': 'test_response'})
    client = MagicMock()

    fake_env = {
        'SCORECARD_API_KEY': 'test_api_key',
    }
    with open(fake_env_file, 'w') as file:
        for key, value in fake_env.items():
            set_key(fake_env_file, key, value)
    load_dotenv(dotenv_path=fake_env_file)

    run_manager = RunManager(test_set=test_set, scoring_config_id=scoring_config_id, runnable=runnable, client=client)

    yield run_manager, client, test_set, scoring_config_id, runnable  

    remove(fake_env_file)

# Test function using the fixture
@patch('scorecard.run_manager.Scorecard')
def test_run_manager(mock_scorecard, run_manager_setup_teardown):
    run_manager, client, test_set, scoring_config_id, runnable = run_manager_setup_teardown

    mock_run = Run(id=1, 
               scoring_config_id=scoring_config_id, 
               testset_id=test_set, 
               status=RunStatus.RUNNING_EXECUTION, 
               created_at=datetime.now(),
               updated_at=None,
               scoring_start_time=None, 
               scoring_end_time=None,
               execution_start_time=datetime.now(),
               execution_end_time=None,
               limit_testcases=None,
               source=None,
               model_params=None,
               notes=None,
               prompt_template=None)

    client.run.create.return_value = mock_run
    client.run.update_status.return_value = mock_run.copy(update={'status': RunStatus.AWAITING_SCORING})
    test_cases_response = MagicMock()
    test_cases_response.results = [
        TestCase(id=1, testset_id=test_set, user_query='query1', created_at=None, context="context 1", ideal=None, custom_inputs=None, custom_labels=None),
        TestCase(id=2, testset_id=test_set, user_query='query2', created_at=None, context="context 2", ideal=None, custom_inputs=None, custom_labels=None)
    ]
    client.testset.get_testcases.return_value = test_cases_response

    # Mock the runnable to simulate execution
    runnable.side_effect = lambda testcase: TestOutput(context=testcase.context, response=f'response to {testcase.user_query}')

    # Execute the method under test
    run, url = run_manager.run()

    # Assertions
    client.run.create.assert_called_once_with(testset_id=test_set, scoring_config_id=scoring_config_id)
    client.run.update_status.assert_called_with(run_id=mock_run.id, status=RunStatus.AWAITING_SCORING)

    client.testset.get_testcases.assert_called_once_with(testset_id=test_set)
    assert client.testset.get_testcases.return_value.results == test_cases_response.results
    assert len(client.testset.get_testcases.return_value.results) == 2
    # Ensure test records are created for each test case
    assert client.testrecord.create.call_count == 2

    assert run != mock_run
    assert run.status == RunStatus.AWAITING_SCORING
    assert url == f"https://app.getscorecard.ai/view-records/{run.id}"