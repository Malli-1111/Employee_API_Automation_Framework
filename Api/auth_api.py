from Api.base_api import BaseAPI


class AuthAPI:

    @staticmethod
    def login(username="admin", password="admin123", return_response=False):

        payload = {
            "username": username,
            "password": password
        }

        response = BaseAPI.post(
            "/login",
            data=payload
        )

        if return_response:
            return response

        assert response.status_code == 200
        return response.json()["access_token"]