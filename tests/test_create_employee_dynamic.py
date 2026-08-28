"""
Dynamic employee creation API test cases.

This module validates employee creation using dynamically
generated test data provided by the FakeData utility.
"""

from Api.employee_api import EmployeeAPI
from utils.fake_data import FakeData


def test_create_employee_dynamic(auth_headers):
    """
    Verify that an employee can be created using dynamic test data.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    The test generates a randomized employee payload using
    FakeData and validates that the API returns the same
    employee information that was submitted.
    """

    payload = FakeData.employee_payload()

    response = EmployeeAPI.create_employee(
        payload,
        auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["department"] == payload["department"]
    assert data["salary"] == payload["salary"]

    print(data)