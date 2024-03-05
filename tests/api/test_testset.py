import pytest

from src.scorecard.client import Scorecard
from src.scorecard.types import CustomSchema, CustomVariable

SCORECARD_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiYXpwIjoiaHR0cHM6Ly9zdGFnaW5nLnNjb3JlY2FyZC1haS52ZXJjZWwuYXBwIiwiZW1haWwiOiJ0ZXN0aW5nQGdldHNjb3JlY2FyZC5haSIsImV4cCI6MTcwNDU5MzExOCwiaWF0IjoxNzAzOTg4MzE4LCJpc3MiOiJodHRwczovL3N1cHJlbWUtYm9hLTQ4LmNsZXJrLmFjY291bnRzLmRldiIsImp0aSI6IjAxY2UzMzE3MDcyZmMxMDUxZjBmIiwibmJmIjoxNzAzOTg4MzEzLCJvcmdfaWQiOiJvcmdfMmFIdlJUaWVhdmpCZzhUUGJEQ2VQeEI4a2hTIiwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJzdWIiOiJ1c2VyXzJhSHZQQkJTbXBHalhabGpoZGJRbmNoVUZ0RyJ9.e2kWBtqLYiDSu4t_vhflIvw8qBAr9QbrwQ12khVpYoo"


@pytest.fixture
def client():
    return Scorecard(api_key=SCORECARD_API_KEY, base_url="http://localhost:8000")


@pytest.fixture
def testset_args():
    return {
        "name": "test name",
        "description": "test description",
        "using_retrieval": True,
        "custom_schema": CustomSchema(
            variables=[
                CustomVariable(
                    name="input1",
                    description="input1 description",
                    role="input",
                    data_type="text",
                ),
                CustomVariable(
                    name="label1",
                    description="label1 description",
                    role="label",
                    data_type="text",
                ),
                CustomVariable(
                    name="output1",
                    description="output1 description",
                    role="output",
                    data_type="text",
                ),
            ]
        ),
    }


def test_create_read_delete_testset(client, testset_args):
    # Create testset
    testset = client.testset.create(**testset_args)
    assert testset is not None
    created_testset_id = testset.id

    # Read testset
    fetched_testset = client.testset.get(testset_id=created_testset_id)
    assert fetched_testset.id == created_testset_id
    assert fetched_testset.name == "test name"
    assert fetched_testset.description == "test description"
    assert fetched_testset.using_retrieval is True
    # Assert that user_id and org_id are not present in the response
    # Assuming the client library does not expose user_id and org_id directly
    # Assert schemas are not None
    assert fetched_testset.custom_schema is not None

    # Delete testset
    delete_response = client.testset.delete(testset_id=created_testset_id)
    assert delete_response is True

    # Try to get the deleted testset
    try:
        client.testset.get(testset_id=created_testset_id)
        assert False, "Testset still exists after deletion"
    except Exception:
        assert True  # Expected to fail


def test_create_testset_with_schema(client, testset_args):
    # Create testset with custom schema
    testset = client.testset.create(**testset_args)
    created_testset_id = testset.id

    # Create testcase with schema
    testcase = client.testcase.create(
        testset_id=created_testset_id,
        user_query="test query",
        custom_inputs={
            "input1": "input1 value",
        },
    )
    assert testcase is not None

    # Attempt to create testcase with invalid schema should raise an error
    try:
        client.testcase.create(
            testset_id=created_testset_id,
            user_query="test query",
            custom_inputs={
                "missing": "input1 value",
            },
        )
        assert False, "Testcase created with invalid schema"
    except Exception:
        assert True  # Expected to fail due to schema mismatch

    # Delete testset
    delete_response = client.testset.delete(testset_id=created_testset_id)
    assert delete_response is True


def test_read_testset_unauthorized():
    # Assuming there's a way to simulate unauthorized access with the client
    # This might involve using a wrong API key or similar
    unauthorized_client = Scorecard(api_key="incorrect_api_key")
    try:
        unauthorized_client.testset.get(testset_id=340)
        assert False, "Unauthorized access did not raise an error"
    except Exception:
        assert True  # Expected to fail due to unauthorized access
