"""
FastAPI application for the Employee Management API.

This module defines the REST API endpoints for authentication,
employee CRUD operations, pagination, and file uploads.

The application uses SQLAlchemy for database operations and
JWT-based authentication to protect employee and file-upload
endpoints.
"""

from typing import List
import os
import shutil

from fastapi import (
    Depends,
    FastAPI,
    File,
    HTTPException,
    UploadFile
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth import create_access_token, get_current_user
from app.database import engine, SessionLocal
from app.models import Base, Employee
from app.schemas import EmployeeCreate, EmployeeResponse

# Create database tables when the application starts.
Base.metadata.create_all(bind=engine)

# Create the FastAPI application instance.
app = FastAPI()


@app.get("/")
def home():
    """
    Return a welcome message for the Employee Management API.

    Returns:
        dict: Welcome message.
    """

    return {
        "message": "Welcome to Employee Management API"
    }


@app.post("/employees", response_model=EmployeeResponse, status_code=201)
def create_employee(
    employee: EmployeeCreate,
    current_user: str = Depends(get_current_user)
):
    """
    Create a new employee in the database.

    Args:
        employee: Validated employee creation payload.
        current_user: Authenticated username obtained from the JWT token.

    Returns:
        Employee: Newly created employee record.
    """

    db: Session = SessionLocal()

    new_employee = Employee(
        name=employee.name,
        department=employee.department,
        salary=employee.salary
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    db.close()

    return new_employee


@app.get("/employees", response_model=List[EmployeeResponse])
def get_all_employees(
    page: int = 1,
    limit: int = 5,
    current_user: str = Depends(get_current_user)
):
    """
    Retrieve employees using pagination.

    Args:
        page: Page number to retrieve.
        limit: Maximum number of employees returned per page.
        current_user: Authenticated username obtained from the JWT token.

    Returns:
        list[Employee]: Employees for the requested page.
    """

    db: Session = SessionLocal()

    employees = (
        db.query(Employee)
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    db.close()

    return employees


@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retrieve an employee by ID.

    Args:
        employee_id: Unique employee identifier.
        current_user: Authenticated username obtained from the JWT token.

    Returns:
        Employee: Matching employee record.

    Raises:
        HTTPException: 404 if the employee does not exist.
    """

    db: Session = SessionLocal()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    db.close()

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    current_user: str = Depends(get_current_user)
):
    """
    Update an existing employee.

    Args:
        employee_id: Unique employee identifier.
        employee: Updated employee data.
        current_user: Authenticated username obtained from the JWT token.

    Returns:
        Employee: Updated employee record.

    Raises:
        HTTPException: 404 if the employee does not exist.
    """

    db: Session = SessionLocal()

    existing_employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if existing_employee is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    existing_employee.name = employee.name
    existing_employee.department = employee.department
    existing_employee.salary = employee.salary

    db.commit()
    db.refresh(existing_employee)
    db.close()

    return existing_employee


@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    current_user: str = Depends(get_current_user)
):
    """
    Delete an employee by ID.

    Args:
        employee_id: Unique employee identifier.
        current_user: Authenticated username obtained from the JWT token.

    Returns:
        dict: Successful deletion message.

    Raises:
        HTTPException: 404 if the employee does not exist.
    """

    db: Session = SessionLocal()

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(employee)
    db.commit()
    db.close()

    return {
        "message": "Employee deleted successfully"
    }


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate a user and generate a JWT access token.

    Args:
        form_data: OAuth2 username and password form data.

    Returns:
        dict: JWT access token and token type.

    Raises:
        HTTPException: 401 if the credentials are invalid.
    """

    if (
        form_data.username == "admin"
        and form_data.password == "admin123"
    ):

        access_token = create_access_token(
            {"sub": form_data.username}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )


@app.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    current_user: str = Depends(get_current_user)
):
    """
    Upload a file to the application's uploads directory.

    Args:
        file: Multipart file received from the client.
        current_user: Authenticated username obtained from the JWT token.

    Returns:
        dict: Upload success message and uploaded filename.
    """

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }