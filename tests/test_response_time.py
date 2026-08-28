"""
API response-time validation test cases.

This module validates that the employee retrieval API
responds within the expected performance threshold.
"""

from Api.employee_api import EmployeeAPI


def test_get_employee_response_time(auth_headers, employee_id):
    """
    Verify that employee retrieval responds within two seconds.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.
        employee_id: Employee ID provided by the employee_id fixture.

    Validates:
        - API returns HTTP 200.
        - API response time is less than two seconds.
    """

    response = EmployeeAPI.get_employee(
        employee_id,
        auth_headers
    )

    response_time = response.elapsed.total_seconds()

    print(f"\nResponse Time: {response_time:.3f} seconds")

    assert response.status_code == 200

    assert response_time < 2