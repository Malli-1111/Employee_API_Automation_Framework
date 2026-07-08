from Api.employee_api import EmployeeAPI
from payloads.employee_payload import create_employee_payload
from utils.assertions import EmployeeAssertions

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_create_employee(auth_headers):

    response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    print(response.json())

    EmployeeAssertions.validate_employee_created(
        response,
        create_employee_payload
    )