import pytest

# Get started with writing tests with pytest at https://docs.pytest.org
def test_client() -> None:
    pass
from unittest.mock import patch
import asyncio
from src.scorecard.client import Scorecard, AsyncScorecard
from src.scorecard.core.api_error import ApiError
from src.scorecard.types import RunStatus
@pytest.mark.asyncio
async def test_run_tests_async_success() -> None:
    async with patch("src.scorecard.client.AsyncRunClient.create") as mock_create, \
            patch("src.scorecard.client.AsyncRunClient.update_status") as mock_update_status, \
            patch("src.scorecard.client.AsyncTestsetClient.get_testcases") as mock_get_testcases, \
            patch("src.scorecard.client.AsyncTestrecordClient.create") as mock_testrecord_create:
        mock_create.return_value = asyncio.Future()
        mock_create.return_value.set_result(type('obj', (object,), {'id': 1}))
        mock_update_status.return_value = asyncio.Future()
        mock_update_status.return_value.set_result(None)
        mock_get_testcases.return_value = asyncio.Future()
        mock_get_testcases.return_value.set_result(type('obj', (object,), {'results': [{'id': 1, 'user_query': 'query', 'context': 'context', 'ideal': 'ideal'}]}))
        mock_testrecord_create.return_value = asyncio.Future()
        mock_testrecord_create.return_value.set_result(None)

        async_scorecard = AsyncScorecard(api_key="test")
        await async_scorecard.run_tests(input_testset_id=1, scoring_config_id=1, model_invocation=lambda x: x)

        mock_update_status.assert_called_with(1, status=RunStatus.COMPLETED)
        mock_testrecord_create.assert_called()
def test_run_tests_success() -> None:
    with patch("src.scorecard.client.RunClient.create") as mock_create, \
            patch("src.scorecard.client.RunClient.update_status") as mock_update_status, \
            patch("src.scorecard.client.TestsetClient.get_testcases") as mock_get_testcases, \
            patch("src.scorecard.client.TestrecordClient.create") as mock_testrecord_create:
        mock_create.return_value = type('obj', (object,), {'id': 1})
        mock_update_status.return_value = None
        mock_get_testcases.return_value = type('obj', (object,), {'results': [{'id': 1, 'user_query': 'query', 'context': 'context', 'ideal': 'ideal'}]})
        mock_testrecord_create.return_value = None

        scorecard = Scorecard(api_key="test")
        scorecard.run_tests(input_testset_id=1, scoring_config_id=1, model_invocation=lambda x: x)

        mock_update_status.assert_called_with(1, status=RunStatus.COMPLETED)
        mock_testrecord_create.assert_called()
def test_run_tests_api_error() -> None:
    with patch("src.scorecard.client.RunClient.create", side_effect=ApiError("API Error")):
        scorecard = Scorecard(api_key="test")
        with pytest.raises(ApiError):
            scorecard.run_tests(input_testset_id=1, scoring_config_id=1, model_invocation=lambda x: x)
@pytest.mark.asyncio
async def test_run_tests_async_api_error() -> None:
    with patch("src.scorecard.client.AsyncRunClient.create", side_effect=ApiError("API Error")):
        async_scorecard = AsyncScorecard(api_key="test")
        with pytest.raises(ApiError):
            await async_scorecard.run_tests(input_testset_id=1, scoring_config_id=1, model_invocation=lambda x: x)
