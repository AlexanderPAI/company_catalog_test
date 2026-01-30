# mypy: disable-error-code="call-arg"
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    """Config for getting environment variables"""

    # Database env vars
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str
    postgres_db: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


class AppConfig(BaseSettings):
    """Main app configuration"""

    pass


envs = EnvConfig()
