import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from .config import settings

DATABASE_URL = (
    f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

# Retry connection until DB is ready
max_retries = 10
retry_delay = 3  # seconds
for i in range(max_retries):
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        engine.connect()
        print("Database connection established")
        break
    except OperationalError as e:
        print(f"Database not ready, retrying in {retry_delay} seconds... ({i + 1}/{max_retries})")
        time.sleep(retry_delay)
else:
    raise RuntimeError("Failed to connect to the database after multiple attempts")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from typing import Generator


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
