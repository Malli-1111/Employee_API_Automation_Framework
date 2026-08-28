"""
End-to-end employee workflow test cases.

This module validates the complete employee lifecycle:
create, retrieve, update, delete, and final deletion verification.
"""

from Api.employee_api import EmployeeAPI
from payloads.employee_payload import (
    create_employee_payload,
    update_employee_payload
)
import pytest


@pytest.mark.workflow
@pytest.mark.e2e
@pytest.mark.regression
def test_employee_workflow(auth_headers):
    """
    Verify the complete employee management workflow.

    The workflow performs the following operations:

        1. Create an employee.
        2. Retrieve the created employee.
        3. Update the employee.
        4. Delete the employee.
        5. Verify that the employee no longer exists.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - Employee creation returns HTTP 201.
        - Created employee can be retrieved.
        - Employee details can be updated successfully.
        - Employee can be deleted successfully.
        - Deleted employee cannot be retrieved.
    """

    # Create Employee
    create_response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    assert create_response.status_code == 201

    employee_id = create_response.json()["id"]

    print(f"\nCreated Employee ID: {employee_id}")

    # Get Employee
    get_response = EmployeeAPI.get_employee(
        employee_id,
        auth_headers
    )

    assert get_response.status_code == 200
    assert get_response.json()["id"] == employee_id

    # Update Employee
    update_response = EmployeeAPI.update_employee(
        employee_id,
        update_employee_payload,
        auth_headers
    )

    assert update_response.status_code == 200
    assert update_response.json()["name"] == update_employee_payload["name"]
    assert update_response.json()["department"] == update_employee_payload["department"]
    assert update_response.json()["salary"] == update_employee_payload["salary"]

    # Delete Employee
    delete_response = EmployeeAPI.delete_employee(
        employee_id,
        auth_headers
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Employee deleted successfully"

    # Verify Employee Deleted
    verify_response = EmployeeAPI.get_employee(
        employee_id,
        auth_headers
    )

    assert verify_response.status_code == 404
    assert verify_response.json()["detail"] == "Employee not found"