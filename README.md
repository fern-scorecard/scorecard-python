# Scorecard AI Python Library

[![pypi](https://img.shields.io/pypi/v/scorecard-ai.svg)](https://pypi.python.org/pypi/scorecard-ai)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Installation

Add this dependency to your project's build file:

```bash
pip install scorecard-ai
# or
poetry add scorecard-ai
```

## Usage
We also export an HTTP client so that you can hit our APIs 
directly.

```python
import scorecard

from scorecard.client import Scorecard

client = Scorecard(
  api_key="YOUR_API_KEY" # Defaults to SCORECARD_API_KEY
)

testset = client.testset.create(
  testset_id=1234, 
  user_query="Your prompt...", 
  model_params: {
    "param": "value"
  }
)

print(testset)
```

## Async Client
Use our async cien to make non-blocking requests to the API. 

```python
import scorecard
import asyncio

from scorecard.client import AsyncScorecard

client = AsyncScorecard(
  api_key="YOUR_API_KEY" # Defaults to SCORECARD_API_KEY
)

async def main() -> None:
  testset = await client.testset.create(
    testset_id=1234, 
    user_query="Your prompt...", 
    model_params: {
      "param": "value"
    }
  )

  print(testset)

asyncio.run(main())
```

## Running Tests
The `run_tests` method will load your test cases, 
invoke your models with saved prompts, and record success and failure. This is 
available on both the sync and async client.  

```python 
from scorecard.client import Scorecard

client = Scorecard(
  api_key="YOUR_API_KEY"
)

client.run_tests(
  # Your Testset ID 
  input_testset_id=123,
  # Your Scoring Config ID
  scoring_config_id=456,
  # The model invocation that you would like to test
  model_invocation=lambda prompt: call_model(prompt),
)
```

## Timeouts
By default, the client is configured to have a timeout of 60 seconds. You can customize this value at client instantiation. 

```python
from scorecard.client import Scorecard

scorecard_client = Scorecard(
  api_key="YOUR_API_KEY",
  timeout=15,
)
```

## Handling Exceptions
All exceptions thrown by the SDK will subclass [scorecard.ApiError](./src/scorecard/core/api_error.py). 

```python
from scorecard.core import ApiError
from scorecard import UnprocessableEntityError

try:
  client.testset.get("testset-id")
except UnprocessableEntityError as e: 
  # handle unprocessable entity error
except APIError as e:  
  # handle any api related error
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 422         | `UnprocessableEntityError` |

## Telemetry

If you wish to use the Scorecard telemetry setup, you may choose to add the `telemetry` package extra:

```bash
pip install scorecard-ai[telemetry,instrument-openai]
# or
poetry add scorecard-ai --extras "telemetry instrument-openai"
```

Scorecard's SDK can auto-instrument certain AI tools for you by including them in the extras enumeration:

- `instrument-bedrock`
- `instrument-dspy`
- `instrument-langchain`
- `instrument-llama-index`
- `instrument-mistralai`
- `instrument-openai`

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
