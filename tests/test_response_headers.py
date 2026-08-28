"""
API response header validation test cases.

This module validates that the employee API returns the
expected HTTP response headers and content type.
"""

from Api.employee_api import EmployeeAPI


def test_response_headers(auth_headers, employee_id):
    """
    Verify that the employee API returns the expected response headers.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.
        employee_id: Employee ID provided by the employee_id fixture.

    Validates:
        - API returns HTTP 200.
        - Content type is application/json.
        - Content-Length header is present.
        - Date header is present.
        - Server header is present.
    """

    response = EmployeeAPI.get_employee(
        employee_id,
        auth_headers
    )

    assert response.status_code == 200

    headers = response.headers

    print(headers)

    assert headers["content-type"] == "application/json"

    assert "content-length" in headers

    assert "date" in headers

    assert "server" in headers