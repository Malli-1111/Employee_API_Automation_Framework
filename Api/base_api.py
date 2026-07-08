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
    def get(endpoint, headers=None, params=None):
        logger.info(f"GET Request : {endpoint}")

        if headers:
            logger.info(f"Headers : {headers}")

        if params:
            logger.info(f"Query Params : {params}")

        start_time = time.time()

        try:
            response = session.get(
                f"{BASE_URL}{endpoint}",
                headers=headers,
                params=params,
                timeout=BaseAPI.TIMEOUT
            )

            end_time = time.time()

            logger.info(f"Status Code : {response.status_code}")

            try:
                logger.info(f"Response : {response.json()}")
            except Exception:
                logger.info(f"Response : {response.text}")

            logger.info(f"Execution Time : {end_time-start_time:.3f} sec")

            return response

        except requests.exceptions.RequestException as e:
            logger.error(f"GET Request Failed : {e}")
            raise

    @staticmethod
    def post(endpoint, json=None, data=None, files=None, headers=None):

        logger.info(f"POST Request : {endpoint}")

        if json:
            logger.info(f"JSON Payload : {json}")

        if data:
            logger.info(f"Form Data : {data}")

        if files:
            logger.info(f"Uploading File")    

        if headers:
            logger.info(f"Headers : {headers}")

        start_time = time.time()

        try:

            response = session.post(
                f"{BASE_URL}{endpoint}",
                json=json,
                data=data,
                files=files,
                headers=headers,
                timeout=BaseAPI.TIMEOUT
            )

            end_time = time.time()

            logger.info(f"Status Code : {response.status_code}")

            try:
                logger.info(f"Response : {response.json()}")
            except Exception:
                logger.info(f"Response : {response.text}")

            logger.info(f"Execution Time : {end_time - start_time:.3f} sec")

            return response

        except requests.exceptions.RequestException as e:

            logger.error(f"POST Request Failed : {e}")

            raise

    @staticmethod
    def put(endpoint, json=None, headers=None):

        logger.info(f"PUT Request : {endpoint}")

        if json:
            logger.info(f"JSON Payload : {json}")

        if headers:
            logger.info(f"Headers : {headers}")

        start_time = time.time()

        try:

            response = session.put(
                f"{BASE_URL}{endpoint}",
                json=json,
                headers=headers,
                timeout=BaseAPI.TIMEOUT
            )

            end_time = time.time()

            logger.info(f"Status Code : {response.status_code}")

            try:
                logger.info(f"Response : {response.json()}")
            except Exception:
                logger.info(f"Response : {response.text}")

            logger.info(f"Execution Time : {end_time - start_time:.3f} sec")

            return response

        except requests.exceptions.RequestException as e:

            logger.error(f"PUT Request Failed : {e}")

            raise

    @staticmethod
    def delete(endpoint, headers=None):

        logger.info(f"DELETE Request : {endpoint}")

        if headers:
            logger.info(f"Headers : {headers}")

        start_time = time.time()

        try:

            response = requests.delete(
                f"{BASE_URL}{endpoint}",
                headers=headers,
                timeout=BaseAPI.TIMEOUT
            )

            end_time = time.time()

            logger.info(f"Status Code : {response.status_code}")

            try:
                logger.info(f"Response : {response.json()}")
            except Exception:
                logger.info(f"Response : {response.text}")

            logger.info(f"Execution Time : {end_time - start_time:.3f} sec")

            return response

        except requests.exceptions.RequestException as e:

            logger.error(f"DELETE Request Failed : {e}")

            raise