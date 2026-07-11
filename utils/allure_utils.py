import json
import allure


class AllureUtils:

    @staticmethod
    def attach_request(
        method,
        url,
        headers=None,
        params=None,
        json_payload=None,
        data=None
    ):
        """
        Attach API request details to the Allure report.
        """

        with allure.step(f"{method} Request"):

            allure.attach(
                method,
                "HTTP Method",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                url,
                "URL",
                attachment_type=allure.attachment_type.TEXT
            )

            if headers:
                allure.attach(
                    json.dumps(dict(headers), indent=4),
                    "Headers",
                    attachment_type=allure.attachment_type.JSON
                )

            if params:
                allure.attach(
                    json.dumps(params, indent=4),
                    "Query Parameters",
                    attachment_type=allure.attachment_type.JSON
                )

            if json_payload:
                allure.attach(
                    json.dumps(json_payload, indent=4),
                    "Request Payload",
                    attachment_type=allure.attachment_type.JSON
                )

            if data:
                allure.attach(
                    str(data),
                    "Form Data",
                    attachment_type=allure.attachment_type.TEXT
                )

    @staticmethod
    def attach_response(
        response,
        execution_time
    ):
        """
        Attach API response details to the Allure report.
        """

        with allure.step("Response"):

            allure.attach(
                str(response.status_code),
                "Status Code",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                f"{execution_time:.3f} sec",
                "Execution Time",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                json.dumps(dict(response.headers), indent=4),
                "Response Headers",
                attachment_type=allure.attachment_type.JSON
            )

            try:

                allure.attach(
                    json.dumps(response.json(), indent=4),
                    "Response Body",
                    attachment_type=allure.attachment_type.JSON
                )

            except Exception:

                allure.attach(
                    response.text,
                    "Response Body",
                    attachment_type=allure.attachment_type.TEXT
                )

    @staticmethod
    def attach_exception(exception):
        """
        Attach exception details to the Allure report.
        """

        allure.attach(
            str(exception),
            "Exception",
            attachment_type=allure.attachment_type.TEXT
        )