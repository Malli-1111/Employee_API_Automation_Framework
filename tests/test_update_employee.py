from Api.employee_api import EmployeeAPI
from payloads.employee_payload import update_employee_payload
from utils.assertions import EmployeeAssertions


def test_update_employee(employee_id, auth_headers):

    response = EmployeeAPI.update_employee(
        employee_id,
        update_employee_payload,
        auth_headers
    )

    EmployeeAssertions.validate_employee_updated(
        response,
        employee_id,
        update_employee_payload
    )


def test_update_invalid_employee(auth_headers):

    response = EmployeeAPI.update_employee(
        999,
        update_employee_payload,
        auth_headers
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


def test_update_invalid_datatype(auth_headers):

    response = EmployeeAPI.update_employee(
        "abc",
        update_employee_payload,
        auth_headers
    )

    assert response.status_code == 422