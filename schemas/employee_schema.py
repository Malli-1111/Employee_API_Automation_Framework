"""
Employee response schema for API test validation.

This module defines the expected structure and data types
of an employee API response.
"""

from pydantic import BaseModel


class EmployeeSchema(BaseModel):
    """
    Defines the expected structure of an employee response.

    Used to validate that employee API responses contain the
    required fields with the expected data types.
    """

    id: int
    name: str
    department: str
    salary: float