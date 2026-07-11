from Api.employee_api import EmployeeAPI
from payloads.employee_payload import create_employee_payload
from utils.assertions import EmployeeAssertions

import pytest
import allure


@pytest.mark.smoke
@pytest.mark.regression

@allure.feature("Employee Management")
@allure.story("Create Employee")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create employee with valid data")
@allure.description(
    "Verify that a new employee can be created successfully using valid employee details."
)
def test_create_employee(auth_headers):

    response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    EmployeeAssertions.validate_employee_created(
        response,
        create_employee_payload
    )