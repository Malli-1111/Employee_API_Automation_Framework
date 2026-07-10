import requests
import time

from utils.config import BASE_URL
from utils.logger import logger

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

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

    TIMEOUT = 10

    @staticmethod
    def request(
        method,
        endpoint,
        headers=None,
        params=None,
        json=None,
        data=None,
        files=None
    ):

        logger.info(f"{method} Request : {endpoint}")

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

            end_time = time.time()

            logger.info(f"Status Code : {response.status_code}")

            try:
                logger.info(f"Response : {response.json()}")
            except Exception:
                logger.info(f"Response : {response.text}")

            logger.info(
                f"Execution Time : {end_time - start_time:.3f} sec"
            )

            return response

        except requests.exceptions.RequestException as e:

            logger.error(f"{method} Request Failed : {e}")

            raise

    @staticmethod
    def get(endpoint, headers=None, params=None):

        return BaseAPI.request(
            method="GET",
            endpoint=endpoint,
            headers=headers,
            params=params
        )

    @staticmethod
    def post(endpoint, json=None, data=None, files=None, headers=None):

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

        return BaseAPI.request(
            method="PUT",
            endpoint=endpoint,
            headers=headers,
            json=json
        )

    @staticmethod
    def delete(endpoint, headers=None):

        return BaseAPI.request(
            method="DELETE",
            endpoint=endpoint,
            headers=headers
        )