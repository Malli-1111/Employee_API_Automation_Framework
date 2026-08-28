"""
Authentication API client.

Provides reusable methods for authentication-related API operations.
"""
from Api.base_api import BaseAPI


class AuthAPI:
    """Provides reusable authentication API operations."""

    @staticmethod
    def login(username="admin", password="admin123", return_response=False):
        """
        Authenticate a user and retrieve an access token.

        Args:
            username: Login username.
            password: Login password.
            return_response: When True, return the complete response.

        Returns:
          str: Access token when return_response is False.
          requests.Response: Complete response when return_response is True.
        """
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
