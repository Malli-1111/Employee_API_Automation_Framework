import pytest

from Api.employee_api import EmployeeAPI
from Api.auth_api import AuthAPI
from payloads.employee_payload import create_employee_payload

import os

def pytest_addoption(parser):

    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment Name"
    )


def pytest_configure(config):

    env = config.getoption("--env")

    os.environ["TEST_ENV"] = env
    
@pytest.fixture
def access_token():

    token = AuthAPI.login()

    print(f"\nAccess Token: {token}")

    return token


@pytest.fixture
def auth_headers(access_token):

    return {
        "Authorization": f"Bearer {access_token}"
    }


@pytest.fixture
def employee_id(auth_headers):

    response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    print(f"\nCreated Employee ID: {data['id']}")

    return data["id"]