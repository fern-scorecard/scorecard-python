from scorecard.client import Scorecard

client = Scorecard(
    base_url="http://localhost:8000",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiYXpwIjoiaHR0cHM6Ly9hcHAuZ2V0c2NvcmVjYXJkLmFpIiwiZW1haWwiOiJ0ZWFtQGdldHNjb3JlY2FyZC5haSIsImV4cCI6MTk2MzY0MjcwOSwiaWF0IjoxNzA0NDQyNzA5LCJpc3MiOiJodHRwczovL2NsZXJrLmdldHNjb3JlY2FyZC5haSIsImp0aSI6IjI4OTk1YjM3MWViMzFjMmQ3MTg3IiwibmJmIjoxNzA0NDQyNzA0LCJvcmdfaWQiOiJvcmdfMlZnQ2syREdTUUhUb2pFSTNPVk5IOGszT2tIIiwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJzdWIiOiJ1c2VyXzJWNWg0OTVua3NzRkFrdFoweVhEeENjbDEySyJ9.rpd1nz8r539hrJ29CLoLnwxdyEZRhkjk_VA_oeBUCZg",
)

run = client.run.create(testset_id=395, scoring_config_id=34)
client.run.update_status(run.id, status="running_execution")
testcases = client.testset.get_testcases(395)

for testcase in testcases.results:
    if testcase.id is None:
        continue

    testcase_id = testcase.id
    query = testcase.user_query

    print(f"Running testcase {testcase_id}...")
    print(f"User query: {query}")

    response = query + " response"

    client.testrecord.create(
        run_id=run.id,
        testcase_id=testcase_id,
        testset_id=395,
        user_query=testcase.user_query,
        context=testcase.context,
        ideal=testcase.ideal,
        response=response,
    )

client.run.update_status(run.id, status="completed")

print("Finished running testcases.")

# async def run_tests():
#     await client.run_tests(
#         # Your Testset ID
#         input_testset_id=395,
#         # Your Scoring Config ID
#         scoring_config_id=34,
#         # The model invocation that you would like to test
#         model_invocation=lambda prompt: prompt,
#     )


# # Run the async function
# asyncio.run(run_tests())
