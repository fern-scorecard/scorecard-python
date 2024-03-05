from pydantic import BaseModel, Field, ConfigDict, PlainSerializer, computed_field
from pydantic_settings import SettingsConfigDict, BaseSettings
from datetime import datetime, timedelta
from supabase._sync.client import create_client
from postgrest.exceptions import APIError
from postgrest.base_request_builder import APIResponse
from postgrest._sync.request_builder import SyncRequestBuilder
from typing import Annotated, Dict, TypeVar, Generic, Type, List
from threading import Lock

from tracer.log_object import Input, InputArgument, Output

BaseSchemaT = TypeVar("BaseSchemaT", bound="BaseSchema")


class Table(Generic[BaseSchemaT]):

    def __init__(self, schema: Type[BaseSchemaT]) -> None:
        self.schema = schema
        self.client = create_client(Settings().url, Settings().key)
        self.table: SyncRequestBuilder = self.client.table(self.schema.__name__.lower())
        self.lock = Lock()

    def insert(self, data: BaseSchemaT) -> List[BaseSchemaT]:
        try:
            response = self.table.insert(data.model_dump(exclude_none=True)).execute()
        except Exception as e:
            # this is a silent failure and that is bad. But more on this later.
            return []
        else:
            return [self.schema.model_validate(record) for record in response.data]

    def sync_insert_no_check(self, data: BaseSchemaT):
        with self.lock:
            self.table.insert(data.model_dump(exclude_none=True)).execute()

    def get(self, id: int) -> BaseSchemaT:
        print(self.schema.__name__.lower())
        response: APIResponse = self.table.select("*").eq("id", id).execute()
        return self.schema.model_validate(response.data[0])

    def get_by(self, **kwargs) -> List[BaseSchemaT]:
        response: APIResponse = self.table.select("*").eq(**kwargs).execute()
        return [self.schema.model_validate(record) for record in response.data]


class BaseSchema(BaseModel):
    model_config = ConfigDict()
    id: int | None = Field(default=None)
    created_at: datetime | None = Field(default=None)

    @classmethod
    def table(cls: Type[BaseSchemaT]) -> Table[BaseSchemaT]:
        return Table(cls)

    def insert(self: BaseSchemaT) -> BaseSchemaT:
        res = self.__class__.table().insert(self)
        if len(res) == 0:
            raise APIError({"message": "Failed to insert record"})
        return res[0]

    @classmethod
    def get(cls: Type[BaseSchemaT], id: int) -> BaseSchemaT:
        return cls.table().get(id)


SerializableDateTime = Annotated[
    datetime, PlainSerializer(lambda x: str(x), return_type=str, when_used="always")
]


SerializableTimeDelta = Annotated[
    timedelta, PlainSerializer(lambda x: str(x), return_type=str, when_used="always")
]


class TestSet(BaseSchema):
    name: str
    session: int | None = Field(default=None)

    def add_test_case(self, input: Input) -> "TestCase":
        if self.id is None:
            raise ValueError("TestSet must be saved before adding test cases")
        return TestCase(input=input, testset=self.id).insert()

    def get_test_cases(self) -> List["TestCase"]:
        res: APIResponse = (
            TestCase.table().table.select("*").eq("testset", self.id).execute()
        )
        return [TestCase.model_validate(record) for record in res.data]


class TestCase(BaseSchema):
    input: Input
    testset: int

    def record(self, output: Output) -> "TestRecord":
        if self.id is None:
            raise ValueError("TestCase must be saved before adding test records")
        return TestRecord(output=output, testcase=self.id).insert()


class TestRecord(BaseSchema):
    output: Output
    testcase: int


class LogRecord(BaseSchema):
    trace_id: str
    parent_span_id: str | None
    span_id: str
    function_name: str
    start_time: SerializableDateTime
    end_time: SerializableDateTime
    inputs: List[InputArgument] = Field(default_factory=list)
    output: Output
    session: int

    @computed_field  # type: ignore[misc]
    @property
    def execution_time(self) -> SerializableTimeDelta:
        return self.end_time - self.start_time


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="SUPABASE_"
    )

    url: str = ""
    key: str = ""


class Session(BaseSchema):
    tags: Dict[str, str] = Field(default_factory=dict)


if __name__ == "__main__":

    for case in TestSet.get(id=11).get_test_cases():
        print(case.input.jsonify())
