"""
Employee retrieval API test cases.

This module validates successful employee retrieval,
non-existent employee handling, and invalid employee ID
data-type validation.
"""

from Api.employee_api import EmployeeAPI
from utils.assertions import EmployeeAssertions


def test_get_employee(employee_id, auth_headers):
    """
    Verify that an existing employee can be retrieved by ID.

    Args:
        employee_id: Employee ID provided by the employee_id fixture.
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - Employee retrieval is successful.
        - Returned employee ID matches the requested ID.
    """

    response = EmployeeAPI.get_employee(
        employee_id,
        auth_headers
    )

    EmployeeAssertions.validate_employee_retrieved(
        response,
        employee_id
    )


def test_get_invalid_employee(auth_headers):
    """
    Verify that requesting a non-existent employee returns HTTP 404.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - API returns HTTP 404.
        - API returns the expected employee-not-found message.
    """

    response = EmployeeAPI.get_employee(
        999,
        auth_headers
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


def test_get_employee_invalid_datatype(auth_headers):
    """
    Verify that an invalid employee ID data type is rejected.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - API returns HTTP 422 for an invalid employee ID type.
    """

    response = EmployeeAPI.get_employee(
        "abc",
        auth_headers
    )

    assert response.status_code == 422