"""
Employee API client.

Provides reusable methods for employee CRUD operations.
"""
from Api.base_api import BaseAPI


class EmployeeAPI:
    """Provides reusable employee CRUD operations."""

    @staticmethod
    def create_employee(payload, headers=None):
        """
        Create a new employee.

        Args:
          payload: Employee request payload.
          headers: Optional HTTP headers.

        Returns:
          requests.Response: API response.
        """
        return BaseAPI.post(
            "/employees",
            json=payload,
            headers=headers
        )

    @staticmethod
    def get_employee(employee_id, headers=None):
        """
    Retrieve an employee by ID.

    Args:
        employee_id: The ID of the employee to retrieve.
        headers: Optional HTTP headers.

    Returns:
        requests.Response: API response.
    """
        return BaseAPI.get(
            f"/employees/{employee_id}",
            headers=headers
        )

    @staticmethod
    def update_employee(employee_id, payload, headers=None):
        """
    Update an existing employee.

    Args:
        employee_id: Unique employee identifier..
        payload: Employee request payload.
        headers: Optional HTTP headers.

    Returns:
        requests.Response: API response.
    """
        return BaseAPI.put(
            f"/employees/{employee_id}",
            json=payload,
            headers=headers
        )

    @staticmethod
    def delete_employee(employee_id, headers=None):
        """
    Delete an employee by ID.

    Args:
        employee_id: The ID of the employee to delete.
        headers: Optional HTTP headers.

    Returns:
        requests.Response: API response.
    """
        return BaseAPI.delete(
            f"/employees/{employee_id}",
            headers=headers
        )
    @staticmethod
    def get_all_employees(headers=None, params=None):
        """
        Retrieve all employees.

        Args:
            headers: Optional HTTP headers.
            params: Optional query parameters.

        Returns:
            requests.Response: API response.
        """
        return BaseAPI.get(
        "/employees",
        headers=headers,
        params=params
       )