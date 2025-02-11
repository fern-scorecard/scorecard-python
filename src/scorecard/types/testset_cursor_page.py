# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .testset import Testset
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TestsetCursorPage(UncheckedBaseModel):
    items: typing.List[Testset]
    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total items
    """

    current_page: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor to refetch the current page
    """

    current_page_backwards: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor to refetch the current page starting from the last item
    """

    previous_page: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor for the previous page
    """

    next_page: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor for the next page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
