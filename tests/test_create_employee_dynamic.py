from Api.employee_api import EmployeeAPI
from utils.fake_data import FakeData


def test_create_employee_dynamic(auth_headers):

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