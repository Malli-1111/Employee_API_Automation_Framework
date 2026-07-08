from Api.employee_api import EmployeeAPI


def test_response_headers(auth_headers, employee_id):

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