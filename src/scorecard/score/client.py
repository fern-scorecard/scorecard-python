# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.grade import Grade
from ..types.http_validation_error import HttpValidationError
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.unauthenticated_error import UnauthenticatedError
from ..types.unauthorized_error_body import UnauthorizedErrorBody

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ScoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        run_id: int,
        testrecord_id: int,
        *,
        metric_id: int,
        int_score: typing.Optional[int] = OMIT,
        binary_score: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Grade:
        """
        Create a score

        Parameters
        ----------
        run_id : int

        testrecord_id : int

        metric_id : int

        int_score : typing.Optional[int]

        binary_score : typing.Optional[bool]

        reasoning : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grade
            Successful Response

        Examples
        --------
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.score.create(
            run_id=1,
            testrecord_id=1,
            metric_id=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"metric_id": metric_id}
        if int_score is not OMIT:
            _request["int_score"] = int_score
        if binary_score is not OMIT:
            _request["binary_score"] = binary_score
        if reasoning is not OMIT:
            _request["reasoning"] = reasoning
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/run/{jsonable_encoder(run_id)}/testrecord/{jsonable_encoder(testrecord_id)}/score",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(Grade, construct_type(type_=Grade, object_=_response.json()))  # type: ignore
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

    def update(
        self,
        run_id: int,
        testrecord_id: int,
        score_id: int,
        *,
        int_score: typing.Optional[int] = OMIT,
        binary_score: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Grade:
        """
        Update a score

        Parameters
        ----------
        run_id : int

        testrecord_id : int

        score_id : int

        int_score : typing.Optional[int]

        binary_score : typing.Optional[bool]

        reasoning : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grade
            Successful Response

        Examples
        --------
        from scorecard.client import Scorecard

        client = Scorecard(
            api_key="YOUR_API_KEY",
        )
        client.score.update(
            run_id=1,
            testrecord_id=1,
            score_id=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if int_score is not OMIT:
            _request["int_score"] = int_score
        if binary_score is not OMIT:
            _request["binary_score"] = binary_score
        if reasoning is not OMIT:
            _request["reasoning"] = reasoning
        _response = self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/run/{jsonable_encoder(run_id)}/testrecord/{jsonable_encoder(testrecord_id)}/score/{jsonable_encoder(score_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(Grade, construct_type(type_=Grade, object_=_response.json()))  # type: ignore
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


class AsyncScoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        run_id: int,
        testrecord_id: int,
        *,
        metric_id: int,
        int_score: typing.Optional[int] = OMIT,
        binary_score: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Grade:
        """
        Create a score

        Parameters
        ----------
        run_id : int

        testrecord_id : int

        metric_id : int

        int_score : typing.Optional[int]

        binary_score : typing.Optional[bool]

        reasoning : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grade
            Successful Response

        Examples
        --------
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.score.create(
            run_id=1,
            testrecord_id=1,
            metric_id=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"metric_id": metric_id}
        if int_score is not OMIT:
            _request["int_score"] = int_score
        if binary_score is not OMIT:
            _request["binary_score"] = binary_score
        if reasoning is not OMIT:
            _request["reasoning"] = reasoning
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/run/{jsonable_encoder(run_id)}/testrecord/{jsonable_encoder(testrecord_id)}/score",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(Grade, construct_type(type_=Grade, object_=_response.json()))  # type: ignore
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

    async def update(
        self,
        run_id: int,
        testrecord_id: int,
        score_id: int,
        *,
        int_score: typing.Optional[int] = OMIT,
        binary_score: typing.Optional[bool] = OMIT,
        reasoning: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Grade:
        """
        Update a score

        Parameters
        ----------
        run_id : int

        testrecord_id : int

        score_id : int

        int_score : typing.Optional[int]

        binary_score : typing.Optional[bool]

        reasoning : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Grade
            Successful Response

        Examples
        --------
        from scorecard.client import AsyncScorecard

        client = AsyncScorecard(
            api_key="YOUR_API_KEY",
        )
        await client.score.update(
            run_id=1,
            testrecord_id=1,
            score_id=1,
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if int_score is not OMIT:
            _request["int_score"] = int_score
        if binary_score is not OMIT:
            _request["binary_score"] = binary_score
        if reasoning is not OMIT:
            _request["reasoning"] = reasoning
        _response = await self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"v1/run/{jsonable_encoder(run_id)}/testrecord/{jsonable_encoder(testrecord_id)}/score/{jsonable_encoder(score_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(Grade, construct_type(type_=Grade, object_=_response.json()))  # type: ignore
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
