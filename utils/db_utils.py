"""
Database utility module for backend validation.

Provides database connectivity and reusable queries for validating
API results against the SQLite database.
"""
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
    """Provides reusable database queries for test validation."""

    @staticmethod
    def get_employee(employee_id):
        """
        Retrieve an employee from the database using the employee ID.

        Args:
            employee_id: Unique employee identifier.

        Returns:
            Employee | None: Matching employee record, or None if not found.
        """

        db = SessionLocal()

        try:
            employee = db.query(Employee).filter(
                Employee.id == employee_id
            ).first()

            return employee

        finally:
            db.close()