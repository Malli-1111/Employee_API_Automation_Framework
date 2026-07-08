from Api.auth_api import AuthAPI
import pytest

@pytest.mark.login
@pytest.mark.smoke
def test_valid_login():

    token = AuthAPI.login()

    assert token is not None
    assert isinstance(token, str)


@pytest.mark.login
@pytest.mark.regression
def test_invalid_username():

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

    response = AuthAPI.login(
        username="",
        password="",
        return_response=True
    )
    print(response.status_code)
    print(response.text)

    assert response.status_code == 422