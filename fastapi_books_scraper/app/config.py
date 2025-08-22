from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DB_HOST: str = Field(default="db")
    DB_PORT: int = Field(default=5432)
    DB_NAME: str = Field(default="booksdb")
    DB_USER: str = Field(default="booksuser")
    DB_PASSWORD: str = Field(default="bookspass")
    SCRAPE_BASE_URL: str = Field(default="http://books.toscrape.com/")
    USER_AGENT: str = Field(default="Mozilla/5.0 (compatible; FastAPI-Scraper/1.0; +https://example.com)")
    REQUEST_DELAY_SEC: float = Field(default=0.5)

    class Config:
        env_file = ".env"


settings = Settings()
