import pytest

from Api.upload_api import UploadAPI


@pytest.mark.smoke
@pytest.mark.regression
def test_upload_file(auth_headers):

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