import pytest

from Api.employee_api import EmployeeAPI
from utils.json_reader import read_json

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

    response = EmployeeAPI.create_employee(
        payload,
        auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["department"] == payload["department"]
    assert data["salary"] == payload["salary"]