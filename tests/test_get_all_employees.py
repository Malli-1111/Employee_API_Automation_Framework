from Api.employee_api import EmployeeAPI


def test_get_all_employees(auth_headers):

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