import sys
from pydantic import BaseSettings
from functools import lru_cache
from url_shortener_app.exception import URLShortnerException

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"
    
class Config:
        env_file = ".env"

@lru_cache
# @lru_cache decorator allows you to cache the result of get_settings() using the LRU strategy.
def get_settings() -> Settings:
    try:
        settings = Settings()
        print(f"Loading settings for: {settings.env_name}")
        return settings
    except Exception as e:
        raise URLShortnerException(e,sys)