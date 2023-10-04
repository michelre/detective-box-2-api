from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_uri: str
    secret_key: str
    admin_token: str
    model_config = ConfigDict(env_file=".env")


settings = Settings()
