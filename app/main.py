from typing import List

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal
from app.models import Base, Employee
from app.schemas import (
    EmployeeCreate,
    EmployeeResponse,
    LoginRequest
)
from app.auth import create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
from fastapi import UploadFile, File
import shutil
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management API"
    }


@app.post("/employees", response_model=EmployeeResponse, status_code=201)
def create_employee(
    employee: EmployeeCreate,
    current_user: str = Depends(get_current_user)
):

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

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }