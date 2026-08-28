"""
File upload API test cases.

This module validates successful file upload through the
Employee Management API.
"""

import pytest

from Api.upload_api import UploadAPI


@pytest.mark.smoke
@pytest.mark.regression
def test_upload_file(auth_headers):
    """
    Verify that a file can be uploaded successfully.

    Args:
        auth_headers: Authorization headers provided by the
            authentication fixture.

    Validates:
        - File upload returns HTTP 200.
        - API returns the expected success message.
        - API returns the uploaded filename.
    """

    response = UploadAPI.upload(
        endpoint="/upload",
        file_path="resources/sample.txt",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "File uploaded successfully"

    assert data["filename"] == "sample.txt"

    print(data)