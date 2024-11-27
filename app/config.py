from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()
