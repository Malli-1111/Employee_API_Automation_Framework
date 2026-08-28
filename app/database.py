"""
Database configuration for the FastAPI application.

This module configures the SQLite database connection and
provides the SQLAlchemy engine, session factory, and declarative
base used by the application's database models.
"""
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SQLite database
DATABASE_PATH = BASE_DIR / "employee.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()