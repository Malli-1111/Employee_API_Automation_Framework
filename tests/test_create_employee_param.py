"""
Parameterized employee creation API test cases.

This module validates employee creation using multiple
predefined payloads supplied through Pytest parameterization.
"""

import pytest

from Api.employee_api import EmployeeAPI


@pytest.mark.parametrize(
    "payload",
    [
        {
            "name": "Rahul",
            "department": "QA",
            "salary": 50000
        },
        {
            "name": "Naresh",
            "department": "Developer",
            "salary": 70000
        },
        {
            "name": "Ravi",
            "department": "DevOps",
            "salary": 80000
        }
    ]
)
def test_create_employee(auth_headers, payload):
    """
    Verify employee creation using multiple predefined payloads.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.
        payload: Employee data supplied by pytest parameterization.

    Validates:
        - Each employee creation request returns HTTP 201.
        - Returned employee name matches the submitted name.
        - Returned department matches the submitted department.
        - Returned salary matches the submitted salary.
    """

    response = EmployeeAPI.create_employee(
        payload,
        auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["department"] == payload["department"]
    assert data["salary"] == payload["salary"]