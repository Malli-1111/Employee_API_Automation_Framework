"""
Employee update API test cases.

This module validates successful employee updates,
non-existent employee handling, and invalid employee ID
data-type validation.
"""

from Api.employee_api import EmployeeAPI
from payloads.employee_payload import update_employee_payload
from utils.assertions import EmployeeAssertions
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_update_employee(employee_id, auth_headers):
    """
    Verify that an existing employee can be updated successfully.

    Args:
        employee_id: Employee ID provided by the employee_id fixture.
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - Employee update is successful.
        - Returned employee ID matches the updated employee.
        - Updated employee data matches the request payload.
    """

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
    """
    Verify that updating a non-existent employee returns HTTP 404.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - API returns HTTP 404.
        - API returns the expected employee-not-found message.
    """

    response = EmployeeAPI.update_employee(
        999,
        update_employee_payload,
        auth_headers
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


def test_update_invalid_datatype(auth_headers):
    """
    Verify that an invalid employee ID data type is rejected.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - API returns HTTP 422 for an invalid employee ID type.
    """

    response = EmployeeAPI.update_employee(
        "abc",
        update_employee_payload,
        auth_headers
    )

    assert response.status_code == 422