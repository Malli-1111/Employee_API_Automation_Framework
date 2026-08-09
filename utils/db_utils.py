from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Employee


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Absolute path to employee.db
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


class DBUtils:

    @staticmethod
    def get_employee(employee_id):

        db = SessionLocal()

        try:
            employee = db.query(Employee).filter(
                Employee.id == employee_id
            ).first()

            return employee

        finally:
            db.close()