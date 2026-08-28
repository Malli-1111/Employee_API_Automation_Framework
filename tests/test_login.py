"""
Authentication API test cases.

This module validates successful login, invalid credentials,
and missing credential scenarios for the authentication endpoint.
"""

from Api.auth_api import AuthAPI
import pytest


@pytest.mark.login
@pytest.mark.smoke
def test_valid_login():
    """
    Verify that a valid username and password return an access token.

    Validates:
        - Login is successful.
        - Access token is returned.
        - Access token is a string.
    """

    token = AuthAPI.login()

    assert token is not None
    assert isinstance(token, str)


@pytest.mark.login
@pytest.mark.regression
def test_invalid_username():
    """
    Verify that an invalid username is rejected.

    Validates:
        - API returns HTTP 401.
        - API returns the expected authentication error message.
    """

    response = AuthAPI.login(
        username="wronguser",
        password="admin123",
        return_response=True
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"


@pytest.mark.login
@pytest.mark.regression
def test_invalid_password():
    """
    Verify that an invalid password is rejected.

    Validates:
        - API returns HTTP 401.
        - API returns the expected authentication error message.
    """

    response = AuthAPI.login(
        username="admin",
        password="wrong123",
        return_response=True
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"


@pytest.mark.login
@pytest.mark.regression
def test_blank_username():
    """
    Verify that a blank username is rejected.

    Validates:
        - API returns HTTP 422 for missing/invalid username input.
    """

    response = AuthAPI.login(
        username="",
        password="admin123",
        return_response=True
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 422


@pytest.mark.login
@pytest.mark.regression
def test_blank_password():
    """
    Verify that a blank password is rejected.

    Validates:
        - API returns HTTP 422 for missing/invalid password input.
    """

    response = AuthAPI.login(
        username="admin",
        password="",
        return_response=True
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 422


@pytest.mark.login
@pytest.mark.regression
def test_blank_credentials():
    """
    Verify that blank username and password are rejected.

    Validates:
        - API returns HTTP 422 when both credentials are blank.
    """

    response = AuthAPI.login(
        username="",
        password="",
        return_response=True
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 422