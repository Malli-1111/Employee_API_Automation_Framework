from Api.base_api import BaseAPI


class UploadAPI:

    @staticmethod
    def upload(endpoint, file_path, headers=None):

        with open(file_path, "rb") as file:

            files = {
                "file": file
            }

            return BaseAPI.post(
                endpoint,
                files=files,
                headers=headers
            )