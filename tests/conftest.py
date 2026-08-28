"""
Pytest configuration and reusable fixtures for the API automation framework.

This module manages the FastAPI application lifecycle, environment
configuration, authentication, authorization headers, and reusable
test data fixtures.
"""
import os
import time
import subprocess

import pytest
import requests

from Api.employee_api import EmployeeAPI
from Api.auth_api import AuthAPI
from payloads.employee_payload import create_employee_payload


@pytest.fixture(scope="session", autouse=True)
def start_fastapi():
    """
    Manage the FastAPI application lifecycle for the test session.

    When RUN_IN_DOCKER=true, the fixture assumes FastAPI is already
    running inside a Docker container and waits for the application
    to become available.

    During normal local execution, the fixture starts FastAPI using
    Uvicorn, waits until the Swagger endpoint is available, and
    terminates the server after the test session completes.

    Yields:
        None: Allows the test session to execute after the API is ready.

    Raises:
        RuntimeError: If the FastAPI server fails to become available.
    """

    # When FastAPI is already running in Docker,
    # do not start another server.
    if os.getenv("RUN_IN_DOCKER") == "true":

        print("\n========== USING DOCKER FASTAPI ==========")

        for _ in range(20):

            try:
                response = requests.get(
                    "http://127.0.0.1:8000/docs",
                    timeout=2
                )

                if response.status_code == 200:
                    print(
                        "\n========== DOCKER FASTAPI READY =========="
                    )
                    break

            except requests.exceptions.RequestException:
                pass

            time.sleep(1)

        else:
            raise RuntimeError(
                "Docker FastAPI server is not available."
            )

        yield

        print(
            "\n========== DOCKER FASTAPI IS RUNNING =========="
        )

        return

    # Normal local execution
    print("\n========== STARTING FASTAPI ==========")

    process = subprocess.Popen(
        [
            "python",
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8000",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    server_started = False

    for _ in range(20):

        if process.poll() is not None:
            raise RuntimeError(
                "FastAPI server stopped during startup."
            )

        try:
            response = requests.get(
                "http://127.0.0.1:8000/docs",
                timeout=2
            )

            if response.status_code == 200:
                server_started = True

                print(
                    "\n========== FASTAPI SERVER STARTED =========="
                )

                break

        except requests.exceptions.RequestException:
            pass

        time.sleep(1)

    if not server_started:

        if process.poll() is None:
            process.terminate()
            process.wait()

        raise RuntimeError(
            "FastAPI server failed to start on port 8000."
        )

    yield

    print(
        "\n========== STOPPING FASTAPI SERVER =========="
    )

    if process.poll() is None:
        process.terminate()
        process.wait()

    print(
        "========== FASTAPI SERVER STOPPED =========="
    )


def pytest_addoption(parser):
    """
    Add the custom --env command-line option to Pytest.

    The option allows tests to select an environment-specific
    configuration file such as dev, qa, uat, or prod.
    """

    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment Name"
    )


def pytest_configure(config):
    """
    Configure the selected test environment before test execution.

    Reads the --env Pytest option and stores the selected environment
    in the TEST_ENV environment variable for use by the configuration
    utility.
    """

    env = config.getoption("--env")

    os.environ["TEST_ENV"] = env


@pytest.fixture
def access_token():
    """
    Authenticate through the login API and provide an access token.

    Returns:
        str: JWT access token returned by the authentication API.
    """

    token = AuthAPI.login()

    print(f"\nAccess Token: {token}")

    return token


@pytest.fixture
def auth_headers(access_token):
    """
    Build authorization headers using the generated access token.

    Args:
        access_token: JWT token provided by the access_token fixture.

    Returns:
        dict: Authorization headers for protected API requests.
    """

    return {
        "Authorization": f"Bearer {access_token}"
    }


@pytest.fixture
def employee_id(auth_headers):
    """
    Create an employee and provide its generated ID to dependent tests.

    Args:
        auth_headers: Authorization headers provided by the auth_headers
            fixture.

    Returns:
        int: ID of the newly created employee.

    Raises:
        AssertionError: If employee creation does not return HTTP 201.
    """

    response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    print(f"\nCreated Employee ID: {data['id']}")

    return data["id"]