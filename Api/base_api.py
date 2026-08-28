"""
Common API request layer for the automation framework.

This module provides reusable HTTP request handling, retry configuration,
logging, execution-time measurement, and Allure reporting.
"""
import time
import requests
from utils.allure_utils import AllureUtils

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from utils.config import BASE_URL
from utils.logger import logger

session = requests.Session()

retry = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["GET", "POST", "PUT", "DELETE"]
)

adapter = HTTPAdapter(max_retries=retry)

session.mount("http://", adapter)
session.mount("https://", adapter)


class BaseAPI:
    """
    Provides common HTTP operations for API automation.

    All API-specific classes use this class instead of directly
    calling the requests library.
    """
    TIMEOUT = 10

    @staticmethod
    def request(method, endpoint, headers=None, params=None, json=None, data=None, files=None):
        """
        Send an HTTP request to the configured API endpoint.

        Args:
          method: HTTP method such as GET, POST, PUT, or DELETE.
          endpoint: API endpoint path.
          headers: Optional HTTP headers.
          params: Optional query parameters.
          json: Optional JSON request payload.
          data: Optional form data.
          files: Optional files for multipart upload.

        Returns:
          requests.Response: HTTP response returned by the API.

        Raises:
         requests.exceptions.RequestException:
            If the HTTP request fails.
        """

        logger.info(f"{method} Request : {endpoint}")

        AllureUtils.attach_request(
        method=method,
        url=f"{BASE_URL}{endpoint}",
        headers=headers,
        params=params,
        json_payload=json,
        data=data
        )
    

        if headers:
            logger.info(f"Headers : {headers}")

        if params:
            logger.info(f"Query Params : {params}")

        if json:
            logger.info(f"JSON Payload : {json}")

        if data:
            logger.info(f"Form Data : {data}")

        if files:
            logger.info("Uploading File")

        start_time = time.time()

        try:

            response = session.request(
                method=method,
                url=f"{BASE_URL}{endpoint}",
                headers=headers,
                params=params,
                json=json,
                data=data,
                files=files,
                timeout=BaseAPI.TIMEOUT
            )

            execution_time = time.time() - start_time

            logger.info(f"Status Code : {response.status_code}")

            try:
                logger.info(f"Response : {response.json()}")
            except Exception:
                logger.info(f"Response : {response.text}")

            logger.info(f"Execution Time : {execution_time:.3f} sec")
            AllureUtils.attach_response(
                 response,
                 execution_time
              )
            return response

        except requests.exceptions.RequestException as e:

            logger.error(f"{method} Request Failed : {e}")
            AllureUtils.attach_exception(e)

            raise

    @staticmethod
    def get(endpoint, headers=None, params=None):
        """Send a GET request to the specified endpoint."""
        return BaseAPI.request(
            method="GET",
            endpoint=endpoint,
            headers=headers,
            params=params
        )

    @staticmethod
    def post(endpoint, json=None, data=None, files=None, headers=None):
        """Send a POST request to the specified endpoint."""
        return BaseAPI.request(
            method="POST",
            endpoint=endpoint,
            headers=headers,
            json=json,
            data=data,
            files=files
        )

    @staticmethod
    def put(endpoint, json=None, headers=None):
        """Send a PUT request to the specified endpoint."""
        return BaseAPI.request(
            method="PUT",
            endpoint=endpoint,
            headers=headers,
            json=json
        )

    @staticmethod
    def delete(endpoint, headers=None):
        """Send a DELETE request to the specified endpoint."""
        return BaseAPI.request(
            method="DELETE",
            endpoint=endpoint,
            headers=headers
        )
