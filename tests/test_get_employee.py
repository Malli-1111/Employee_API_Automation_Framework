from Api.employee_api import EmployeeAPI
from utils.assertions import EmployeeAssertions


def test_get_employee(employee_id, auth_headers):

    response = EmployeeAPI.get_employee(
        employee_id,
        auth_headers
    )

    EmployeeAssertions.validate_employee_retrieved(
        response,
        employee_id
    )


def test_get_invalid_employee(auth_headers):

    response = EmployeeAPI.get_employee(
        999,
        auth_headers
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


def test_get_employee_invalid_datatype(auth_headers):

    response = EmployeeAPI.get_employee(
        "abc",
        auth_headers
    )

    assert response.status_code == 422