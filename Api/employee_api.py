from Api.base_api import BaseAPI


class EmployeeAPI:

    @staticmethod
    def create_employee(payload, headers=None):
        return BaseAPI.post(
            "/employees",
            json=payload,
            headers=headers
        )

    @staticmethod
    def get_employee(employee_id, headers=None):
        return BaseAPI.get(
            f"/employees/{employee_id}",
            headers=headers
        )

    @staticmethod
    def update_employee(employee_id, payload, headers=None):
        return BaseAPI.put(
            f"/employees/{employee_id}",
            json=payload,
            headers=headers
        )

    @staticmethod
    def delete_employee(employee_id, headers=None):
        return BaseAPI.delete(
            f"/employees/{employee_id}",
            headers=headers
        )
    @staticmethod
    def get_all_employees(headers=None, params=None):

        return BaseAPI.get(
        "/employees",
        headers=headers,
        params=params
       )