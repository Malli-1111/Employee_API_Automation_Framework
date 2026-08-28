"""
Pydantic schemas for the Employee API.

This module defines request and response models used by FastAPI
for input validation and API response serialization.
"""

from pydantic import BaseModel
class EmployeeCreate(BaseModel):
    """
    Schema for creating an employee.

    Defines the required fields expected in the employee
    creation request.
    """
    name: str
    department: str
    salary: float

class EmployeeResponse(EmployeeCreate):
    """
    Schema for employee API responses.

    Extends EmployeeCreate with the employee's unique ID.
    """

    id: int

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    """
    Schema for login requests.

    Defines the username and password fields required
    for authentication.
    """

    username: str
    password: str