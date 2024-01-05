# Scorecard AI Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

## Installation

Add this dependency to your project's build file:

```bash
pip install fern-scorecard
# or
poetry add fern-scorecard
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
All exceptions thrown by the SDK will sublcass [scorecard.ApiError](./src/scorecard/core/api_error.py). 

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

## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your pyproject.toml file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
