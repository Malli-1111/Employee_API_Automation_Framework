"""
File upload API client.

Provides reusable functionality for multipart file upload operations.
"""
from Api.base_api import BaseAPI


class UploadAPI:
    """Provides reusable file upload API operations."""
    @staticmethod
    def upload(endpoint, file_path, headers=None):
        """
        Upload a file to the specified endpoint.

        Args:
            endpoint (str): The API endpoint for the upload.
            file_path (str): The path to the file to upload.
            headers (dict, optional): Headers to include in the request.

        Returns:
            dict: The response from the API.
        """
        with open(file_path, "rb") as file:

            files = {
                "file": file
            }

            return BaseAPI.post(
                endpoint,
                files=files,
                headers=headers
            )