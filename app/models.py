"""
SQLAlchemy database models for the Employee API.

This module defines the Employee model and maps it to the
employees table in the SQLite database.
"""
from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Employee(Base):
    """
    SQLAlchemy model representing an employee.

    Maps the Employee object to the employees database table.
    """
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    department = Column(String, nullable=False)

    salary = Column(Float, nullable=False)