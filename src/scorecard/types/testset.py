# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel
from .custom_schema import CustomSchema


class Testset(UncheckedBaseModel):
    id: typing.Optional[int] = None
    created_at: typing.Optional[dt.datetime] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    using_retrieval: typing.Optional[bool] = None
    ingestion_method: typing.Optional[str] = None
    num_testcases: typing.Optional[int] = None
    published: typing.Optional[bool] = None
    updated_at: typing.Optional[dt.datetime] = None
    is_archived: typing.Optional[bool] = None
    project_id: typing.Optional[int] = None
    custom_schema: typing.Optional[CustomSchema] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
