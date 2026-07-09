from utils.logger import logger
class EmployeeAssertions:

    @staticmethod
    def validate_employee_created(response, payload):

        assert response.status_code == 201

        data = response.json()

        assert data["name"] == payload["name"]
        assert data["department"] == payload["department"]
        assert data["salary"] == payload["salary"]
        
    @staticmethod
    def validate_employee_retrieved(response, employee_id):

        assert response.status_code == 200

        data = response.json()

        assert data["id"] == employee_id    

    @staticmethod
    def validate_employee_updated(response, employee_id, payload):

        assert response.status_code == 200

        data = response.json()

        assert data["id"] == employee_id
        assert data["name"] == payload["name"]
        assert data["department"] == payload["department"]
        assert data["salary"] == payload["salary"]

    @staticmethod
    def validate_employee_deleted(response):

        assert response.status_code == 200

        data = response.json()

        assert data["message"] == "Employee deleted successfully"

    @staticmethod
    def validate_response_time(response, max_time=2):

        response_time = response.elapsed.total_seconds()

        logger.info(f"\nResponse Time: {response_time:.3f} sec")

        assert response_time < max_time    