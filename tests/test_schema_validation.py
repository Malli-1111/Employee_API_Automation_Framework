"""
API response schema validation test cases.

This module validates that the employee creation response
matches the expected EmployeeSchema structure and data types.
"""

from Api.employee_api import EmployeeAPI
from payloads.employee_payload import create_employee_payload
from schemas.employee_schema import EmployeeSchema


def test_employee_response_schema(auth_headers):
    """
    Verify that the employee API response conforms to the
    expected employee response schema.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - Employee creation returns HTTP 201.
        - API response can be successfully parsed using EmployeeSchema.
        - Generated employee ID is a positive integer.
    """

    response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    # Validate the response structure and field types.
    employee = EmployeeSchema(**data)

    assert employee.id > 0