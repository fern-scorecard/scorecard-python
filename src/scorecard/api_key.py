from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator

class ApiKeyProvider(BaseSettings):
    api_key: str = Field(default="", alias="SCORECARD_API_KEY")
    model_config = SettingsConfigDict(env_prefix="SCORECARD_", env_file=".env")

    @field_validator('api_key')
    def check_api_key(cls, v):
        if not v:
            raise ValueError("SCORECARD_API_KEY must be provided in the environment. Try setting it in your dotenv file.")
        return v


@lru_cache
def get_api_key() -> str:
    return ApiKeyProvider().api_key


if __name__ == "__main__":
    print(get_api_key())