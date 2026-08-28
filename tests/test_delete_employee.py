"""
Employee deletion API test cases.

This module validates successful employee deletion,
non-existent employee handling, and invalid employee ID
data-type validation.
"""

from Api.employee_api import EmployeeAPI
from utils.assertions import EmployeeAssertions


def test_delete_employee(employee_id, auth_headers):
    """
    Verify that an existing employee can be deleted successfully.

    Args:
        employee_id: Employee ID provided by the employee_id fixture.
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - Employee deletion is successful.
        - API response is validated using EmployeeAssertions.
    """

    response = EmployeeAPI.delete_employee(
        employee_id,
        auth_headers
    )

    print(response.json())

    EmployeeAssertions.validate_employee_deleted(
        response
    )


def test_delete_invalid_employee(auth_headers):
    """
    Verify that deleting a non-existent employee returns HTTP 404.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - API returns HTTP 404.
        - API returns the expected employee-not-found message.
    """

    response = EmployeeAPI.delete_employee(
        999,
        auth_headers
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


def test_delete_invalid_datatype(auth_headers):
    """
    Verify that an invalid employee ID data type is rejected.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - API returns HTTP 422 for an invalid employee ID type.
    """

    response = EmployeeAPI.delete_employee(
        "abc",
        auth_headers
    )

    assert response.status_code == 422