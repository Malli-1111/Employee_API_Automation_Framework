from Api.employee_api import EmployeeAPI
from payloads.employee_payload import create_employee_payload
from utils.db_utils import DBUtils


def test_employee_database_validation(auth_headers):

    response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    assert response.status_code == 201

    api_data = response.json()

    db_employee = DBUtils.get_employee(
        api_data["id"]
    )

    assert db_employee is not None
    assert db_employee.id == api_data["id"]
    assert db_employee.name == api_data["name"]
    assert db_employee.department == api_data["department"]
    assert db_employee.salary == api_data["salary"]