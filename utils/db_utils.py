from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Employee


DATABASE_URL = "sqlite:///./employee.db"

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

        employee = db.query(Employee).filter(
            Employee.id == employee_id
        ).first()

        db.close()

        return employee