"""
Reusable assertion utilities for Employee API validation.

This module centralizes common response validations so that
individual test cases remain focused on test scenarios.
"""
from utils.logger import logger
class EmployeeAssertions:
    """Provides reusable assertions for Employee API responses."""

    @staticmethod
    def validate_employee_created(response, payload):
        """
    Validate a successful employee creation response.

    Args:
        response: API response returned by the create employee request.
        payload: Employee data used in the request.

    Validates:
        - HTTP status code is 201.
        - Employee name matches the request payload.
        - Department matches the request payload.
        - Salary matches the request payload.
    """

        assert response.status_code == 201

        data = response.json()

        assert data["name"] == payload["name"]
        assert data["department"] == payload["department"]
        assert data["salary"] == payload["salary"]
        
    @staticmethod
    def validate_employee_retrieved(response, employee_id):
        """
        Validate an employee retrieval response.

        Args:
            response: API response returned by the get employee request.
            employee_id: Expected employee ID.

        Validates:
            - HTTP status code is 200.
            - Returned employee ID matches the requested ID.
        """
        assert response.status_code == 200

        data = response.json()

        assert data["id"] == employee_id    

    @staticmethod
    def validate_employee_updated(response, employee_id, payload):
        """
        Validate a successful employee update response.

        Args:
            response: API response returned by the update request.
            employee_id: Expected employee ID.
            payload: Updated employee data.

        Validates:
            - HTTP status code is 200.
            - Employee ID matches.
            - Updated name matches.
            - Updated department matches.
            - Updated salary matches.
        """
        assert response.status_code == 200

        data = response.json()

        assert data["id"] == employee_id
        assert data["name"] == payload["name"]
        assert data["department"] == payload["department"]
        assert data["salary"] == payload["salary"]

    @staticmethod
    def validate_employee_deleted(response):
        """
        Validate an employee deletion response.

        Args:
            response: API response returned by the delete employee request.

        Validates:
            - HTTP status code is 200.
            - Returned message indicates successful deletion.
        """
        assert response.status_code == 200

        data = response.json()

        assert data["message"] == "Employee deleted successfully"

    @staticmethod
    def validate_response_time(response, max_time=2):
        """
        Validate the response time of an API request.

        Args:
            response: API response returned by the request.
            max_time: Maximum allowed response time in seconds.

        Validates:
            - Response time is less than the maximum allowed time.
        """
        response_time = response.elapsed.total_seconds()

        logger.info(f"\nResponse Time: {response_time:.3f} sec")

        assert response_time < max_time    