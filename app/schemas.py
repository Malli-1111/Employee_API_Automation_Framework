from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: float


class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True
 
class LoginRequest(BaseModel):
    username: str
    password: str        