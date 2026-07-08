from Api.employee_api import EmployeeAPI
from utils.assertions import EmployeeAssertions


def test_delete_employee(employee_id, auth_headers):

    response = EmployeeAPI.delete_employee(
        employee_id,
        auth_headers
    )

    print(response.json())

    EmployeeAssertions.validate_employee_deleted(
        response
    )


def test_delete_invalid_employee(auth_headers):

    response = EmployeeAPI.delete_employee(
        999,
        auth_headers
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


def test_delete_invalid_datatype(auth_headers):

    response = EmployeeAPI.delete_employee(
        "abc",
        auth_headers
    )

    assert response.status_code == 422