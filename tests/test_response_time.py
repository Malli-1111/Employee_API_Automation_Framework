from Api.employee_api import EmployeeAPI


def test_get_employee_response_time(auth_headers, employee_id):

    response = EmployeeAPI.get_employee(
        employee_id,
        auth_headers
    )

    response_time = response.elapsed.total_seconds()

    print(f"\nResponse Time: {response_time:.3f} seconds")

    assert response.status_code == 200

    assert response_time < 2