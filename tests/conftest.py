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

    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment Name"
    )


def pytest_configure(config):

    env = config.getoption("--env")

    os.environ["TEST_ENV"] = env


@pytest.fixture
def access_token():

    token = AuthAPI.login()

    print(f"\nAccess Token: {token}")

    return token


@pytest.fixture
def auth_headers(access_token):

    return {
        "Authorization": f"Bearer {access_token}"
    }


@pytest.fixture
def employee_id(auth_headers):

    response = EmployeeAPI.create_employee(
        create_employee_payload,
        auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    print(f"\nCreated Employee ID: {data['id']}")

    return data["id"]