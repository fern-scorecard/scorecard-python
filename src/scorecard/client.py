# This file was auto-generated by Fern from our API Definition.

import typing

import httpx
import os

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.api_error import ApiError
from .environment import ScorecardEnvironment
from .resources.run.client import AsyncRunClient, RunClient
from .resources.testcase.client import AsyncTestcaseClient, TestcaseClient
from .resources.testrecord.client import AsyncTestrecordClient, TestrecordClient
from .resources.testset.client import AsyncTestsetClient, TestsetClient


class Scorecard:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ScorecardEnvironment = ScorecardEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("SCORECARD_API_KEY"),
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        """
        Instantiate the Scorecard SDK.

        Parameters:
            - base_url: typing.Optional[str]. Overrides the base_url used by the client

            - environment: typing.Optional[ScorecardEnvironment]. Defaults to https://api.getscorecard.ai.

            - api_key: typing.Optional[str]. Your Scorecard API Key. Defaults to the env variable SCORECARD_API_KEY. 

            - timeout: typing.Optional[float]. Defaults to 60 seconds. 

            - httpx_client: typing.Optional[httpx.Client]. Override the httpx client used by the sdk. 
        """
        if api_key is None: 
            raise ApiError(
                body="Please provide an api_key or set SCORECARD_API_KEY")
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.testset = TestsetClient(client_wrapper=self._client_wrapper)
        self.testcase = TestcaseClient(client_wrapper=self._client_wrapper)
        self.run = RunClient(client_wrapper=self._client_wrapper)
        self.testrecord = TestrecordClient(client_wrapper=self._client_wrapper)

class AsyncScorecard:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ScorecardEnvironment = ScorecardEnvironment.DEFAULT,
        api_key: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        """
        Instantiate the Scorecard SDK.

        Parameters:
            - base_url: typing.Optional[str]. Overrides the base_url used by the client

            - environment: typing.Optional[ScorecardEnvironment]. Defaults to https://api.getscorecard.ai.

            - api_key: typing.Optional[str]. Your Scorecard API Key. Defaults to the env variable SCORECARD_API_KEY. 

            - timeout: typing.Optional[float]. Defaults to 60 seconds. 

            - httpx_client: typing.Optional[httpx.AsyncClient]. Override the httpx client used by the sdk. 
        """
        if api_key is None: 
            raise ApiError(
                body="Please provide an api_key or set SCORECARD_API_KEY")
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.testset = AsyncTestsetClient(client_wrapper=self._client_wrapper)
        self.testcase = AsyncTestcaseClient(client_wrapper=self._client_wrapper)
        self.run = AsyncRunClient(client_wrapper=self._client_wrapper)
        self.testrecord = AsyncTestrecordClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: ScorecardEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
