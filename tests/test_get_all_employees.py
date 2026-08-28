"""
Employee collection API test cases.

This module validates retrieval of employees using pagination
parameters.
"""

from Api.employee_api import EmployeeAPI


def test_get_all_employees(auth_headers):
    """
    Verify that employees can be retrieved using pagination.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - API returns HTTP 200.
        - Response body is a list.
        - Number of returned employees does not exceed the
          requested page limit.
    """

    params = {
        "page": 1,
        "limit": 5
    }

    response = EmployeeAPI.get_all_employees(
        headers=auth_headers,
        params=params
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) <= 5