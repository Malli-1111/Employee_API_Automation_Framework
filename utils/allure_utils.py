"""
Allure reporting utilities for the API automation framework.

This module provides reusable methods for attaching API request,
response, and exception details to Allure reports.
"""

import json
import allure

class AllureUtils:
    """
    Provides reusable utilities for Allure API reporting.

    The utility captures request details, response details,
    execution time, and exception information so that API
    test execution can be analyzed directly from the Allure report.
    """

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

        Args:
            method: HTTP method used for the request.
            url: Complete API request URL.
            headers: Optional HTTP request headers.
            params: Optional query parameters.
            json_payload: Optional JSON request payload.
            data: Optional form data.

        The request information is grouped inside an Allure
        step named after the HTTP method.
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

        Args:
            response: HTTP response returned by the API.
            execution_time: Time taken to execute the API request
                in seconds.

        The response status code, execution time, response headers,
        and response body are attached to the Allure report.
        JSON responses are attached as JSON; non-JSON responses
        are attached as plain text.
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

        Args:
            exception: Exception raised during API execution.

        The exception message is attached to the Allure report
        as plain text.
        """

        allure.attach(
            str(exception),
            "Exception",
            attachment_type=allure.attachment_type.TEXT
        )