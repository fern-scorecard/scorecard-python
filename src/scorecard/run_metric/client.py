# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.run_metric import RunMetric
from ..types.unauthenticated_error import UnauthenticatedError
from ..types.unauthorized_error_body import UnauthorizedErrorBody


class RunMetricClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, run_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[RunMetric]:
        """
        Retrieve metrics associated with a run

        Parameters
        ----------
        run_id : int
            The id of the run to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RunMetric]
            Successful Response

        Examples
        --------
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.run_metric.get(
            run_id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/run_metric/{jsonable_encoder(run_id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(typing.List[RunMetric], construct_type(type_=typing.List[RunMetric], object_=_response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                typing.cast(UnauthenticatedError, construct_type(type_=UnauthenticatedError, object_=_response.json()))  # type: ignore
            )
        if _response.status_code == 403:
            raise ForbiddenError(
                typing.cast(UnauthorizedErrorBody, construct_type(type_=UnauthorizedErrorBody, object_=_response.json()))  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(
                typing.cast(NotFoundErrorBody, construct_type(type_=NotFoundErrorBody, object_=_response.json()))  # type: ignore
            )
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRunMetricClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RunMetric]:
        """
        Retrieve metrics associated with a run

        Parameters
        ----------
        run_id : int
            The id of the run to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RunMetric]
            Successful Response

        Examples
        --------
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.run_metric.get(
            run_id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/run_metric/{jsonable_encoder(run_id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(typing.List[RunMetric], construct_type(type_=typing.List[RunMetric], object_=_response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                typing.cast(UnauthenticatedError, construct_type(type_=UnauthenticatedError, object_=_response.json()))  # type: ignore
            )
        if _response.status_code == 403:
            raise ForbiddenError(
                typing.cast(UnauthorizedErrorBody, construct_type(type_=UnauthorizedErrorBody, object_=_response.json()))  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(
                typing.cast(NotFoundErrorBody, construct_type(type_=NotFoundErrorBody, object_=_response.json()))  # type: ignore
            )
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
