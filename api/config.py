from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_uri: str
    secret_key: str
    admin_token: str
    aws_endpoint_url: str
    aws_key_id: str
    aws_secret_key: str
    aws_bucket: str
    mail_key: str
    mail_secret: str
    mail_host: str
    mail_port: int
    model_config = ConfigDict(env_file=".env")


settings = Settings()
