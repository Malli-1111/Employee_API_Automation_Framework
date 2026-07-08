from Api.employee_api import EmployeeAPI
from payloads.employee_payload import create_employee_payload
from schemas.employee_schema import EmployeeSchema


def test_employee_response_schema(auth_headers):

    response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    employee = EmployeeSchema(**data)

    assert employee.id > 0