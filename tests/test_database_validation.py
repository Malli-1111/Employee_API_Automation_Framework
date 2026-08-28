"""
Database validation test cases.

This module validates that employee data returned by the API
is correctly persisted in the database.
"""

from Api.employee_api import EmployeeAPI
from payloads.employee_payload import create_employee_payload
from utils.db_utils import DBUtils


def test_employee_database_validation(auth_headers):
    """
    Verify that an employee created through the API is correctly
    stored in the database.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - Employee creation returns HTTP 201.
        - Employee exists in the database after API creation.
        - Database employee ID matches the API response.
        - Database employee name matches the API response.
        - Database department matches the API response.
        - Database salary matches the API response.
    """

    # Create employee through the API.
    response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    assert response.status_code == 201

    # Capture employee data returned by the API.
    api_data = response.json()

    # Retrieve the same employee directly from the database.
    db_employee = DBUtils.get_employee(
        api_data["id"]
    )

    # Validate that the employee was persisted correctly.
    assert db_employee is not None
    assert db_employee.id == api_data["id"]
    assert db_employee.name == api_data["name"]
    assert db_employee.department == api_data["department"]
    assert db_employee.salary == api_data["salary"]