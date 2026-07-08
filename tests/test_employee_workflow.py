from Api.employee_api import EmployeeAPI
from payloads.employee_payload import (
    create_employee_payload,
    update_employee_payload
)
import pytest

@pytest.mark.workflow
@pytest.mark.e2e
@pytest.mark.regression
def test_employee_workflow(auth_headers):

    # Create Employee
    create_response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    assert create_response.status_code == 201

    employee_id = create_response.json()["id"]

    print(f"\nCreated Employee ID: {employee_id}")

    # Get Employee
    get_response = EmployeeAPI.get_employee(
        employee_id,
        auth_headers
    )

    assert get_response.status_code == 200
    assert get_response.json()["id"] == employee_id

    # Update Employee
    update_response = EmployeeAPI.update_employee(
        employee_id,
        update_employee_payload,
        auth_headers
    )

    assert update_response.status_code == 200
    assert update_response.json()["name"] == update_employee_payload["name"]
    assert update_response.json()["department"] == update_employee_payload["department"]
    assert update_response.json()["salary"] == update_employee_payload["salary"]

    # Delete Employee
    delete_response = EmployeeAPI.delete_employee(
        employee_id,
        auth_headers
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Employee deleted successfully"

    # Verify Employee Deleted
    verify_response = EmployeeAPI.get_employee(
        employee_id,
        auth_headers
    )

    assert verify_response.status_code == 404
    assert verify_response.json()["detail"] == "Employee not found"