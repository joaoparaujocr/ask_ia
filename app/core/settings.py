from pydantic_settings import BaseSettings
from pydantic import SecretStr

class Settings(BaseSettings):
    openai_api_key: SecretStr|None = None
    openai_model: str = "gpt-4o-mini"

    class Config:
        env_file = ".env"

settings = Settings()
