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

    response = EmployeeAPI.create_employee(
        payload,
        auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["department"] == payload["department"]
    assert data["salary"] == payload["salary"]