"""
Data-driven employee creation API test cases.

This module validates employee creation using multiple test
data sets loaded from a JSON file.
"""

import pytest

from Api.employee_api import EmployeeAPI
from utils.json_reader import read_json


# Load employee test data from the JSON test-data file.
employee_data = read_json(
    "test_data/employee_data.json"
)


@pytest.mark.parametrize(
    "payload",
    employee_data
)
@pytest.mark.ddt
@pytest.mark.regression
def test_create_employee(auth_headers, payload):
    """
    Verify employee creation using multiple JSON-based payloads.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.
        payload: Employee test data supplied by pytest parameterization.

    Validates:
        - Employee creation returns HTTP 201.
        - Returned employee name matches the request payload.
        - Returned department matches the request payload.
        - Returned salary matches the request payload.
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