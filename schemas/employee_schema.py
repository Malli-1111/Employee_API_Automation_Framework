from pydantic import BaseModel


class EmployeeSchema(BaseModel):

    id: int
    name: str
    department: str
    salary: float