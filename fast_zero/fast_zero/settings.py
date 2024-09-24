from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = 'E:\\task_manager_fastapi\\task_manager_fastapi\\.env'

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_path, env_file_encoding='utf-8'
    )
    DATABASE_URL: str
