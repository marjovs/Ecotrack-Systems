from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    secret_key: str

    model_config = SettingsConfigDict(env_file='.env')

config = Config()