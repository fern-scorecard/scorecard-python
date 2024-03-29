# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.forbidden_error import ForbiddenError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.run import Run
from ...types.run_status import RunStatus
from ...types.unauthenticated_error import UnauthenticatedError
from ...types.unauthorized_error_body import UnauthorizedErrorBody

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RunClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        testset_id: typing.Optional[int] = OMIT,
        scoring_config_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        model_params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
    ) -> Run:
        """
        Create a new Run

        Parameters:
            - testset_id: typing.Optional[int].

            - scoring_config_id: typing.Optional[int].

            - status: typing.Optional[str].

            - model_params: typing.Optional[typing.Dict[str, typing.Any]].

            - source: typing.Optional[str].

            - notes: typing.Optional[str].

            - prompt_template: typing.Optional[str].
        ---
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.run.create(
            testset_id=1,
            scoring_config_id=2,
            status="RUNNING_EXECUTION",
            model_params={"param1": "value1", "param2": "value2"},
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if testset_id is not OMIT:
            _request["testset_id"] = testset_id
        if scoring_config_id is not OMIT:
            _request["scoring_config_id"] = scoring_config_id
        if status is not OMIT:
            _request["status"] = status
        if model_params is not OMIT:
            _request["model_params"] = model_params
        if source is not OMIT:
            _request["source"] = source
        if notes is not OMIT:
            _request["notes"] = notes
        if prompt_template is not OMIT:
            _request["prompt_template"] = prompt_template
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/run"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Run, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, run_id: int) -> Run:
        """
        Retrieve a Run metadata

        Parameters:
            - run_id: int. The id of the run to retrieve.
        ---
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.run.get(
            run_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/run/{run_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Run, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_status(self, run_id: int, *, status: RunStatus) -> Run:
        """
        Update the status of a run.

        Parameters:
            - run_id: int. The id of the run to update.

            - status: RunStatus.
        ---
        from scorecard import RunStatus
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.run.update_status(
            run_id=1,
            status=RunStatus.PENDING,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/run/{run_id}/status"),
            json=jsonable_encoder({"status": status}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Run, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRunClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        testset_id: typing.Optional[int] = OMIT,
        scoring_config_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        model_params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
    ) -> Run:
        """
        Create a new Run

        Parameters:
            - testset_id: typing.Optional[int].

            - scoring_config_id: typing.Optional[int].

            - status: typing.Optional[str].

            - model_params: typing.Optional[typing.Dict[str, typing.Any]].

            - source: typing.Optional[str].

            - notes: typing.Optional[str].

            - prompt_template: typing.Optional[str].
        ---
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.run.create(
            testset_id=1,
            scoring_config_id=2,
            status="RUNNING_EXECUTION",
            model_params={"param1": "value1", "param2": "value2"},
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if testset_id is not OMIT:
            _request["testset_id"] = testset_id
        if scoring_config_id is not OMIT:
            _request["scoring_config_id"] = scoring_config_id
        if status is not OMIT:
            _request["status"] = status
        if model_params is not OMIT:
            _request["model_params"] = model_params
        if source is not OMIT:
            _request["source"] = source
        if notes is not OMIT:
            _request["notes"] = notes
        if prompt_template is not OMIT:
            _request["prompt_template"] = prompt_template
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/run"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Run, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, run_id: int) -> Run:
        """
        Retrieve a Run metadata

        Parameters:
            - run_id: int. The id of the run to retrieve.
        ---
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.run.get(
            run_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/run/{run_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Run, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_status(self, run_id: int, *, status: RunStatus) -> Run:
        """
        Update the status of a run.

        Parameters:
            - run_id: int. The id of the run to update.

            - status: RunStatus.
        ---
        from scorecard import RunStatus
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.run.update_status(
            run_id=1,
            status=RunStatus.PENDING,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/run/{run_id}/status"),
            json=jsonable_encoder({"status": status}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Run, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(UnauthenticatedError, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(UnauthorizedErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(NotFoundErrorBody, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
