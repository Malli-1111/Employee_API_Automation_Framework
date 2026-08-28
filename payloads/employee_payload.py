"""
Reusable employee request payloads for API testing.

This module contains predefined payloads used by employee
creation and update test scenarios.
"""


# Payload used to create a new employee.
create_employee_payload = {
    "name": "Rahul",
    "department": "QA",
    "salary": 50000
}


# Payload used to update an existing employee.
update_employee_payload = {
    "name": "Rahul",
    "department": "Automation QA",
    "salary": 70000
}