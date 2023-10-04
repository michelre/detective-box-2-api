from pydantic import BaseSettings


class Settings(BaseSettings):
    database_uri: str
    secret_key: str
    admin_token: str

    class Config:
        env_file = ".env"


settings = Settings()
