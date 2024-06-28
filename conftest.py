import pytest
import requests
import helper
import urls


@pytest.fixture(scope="function")
def user():
    user_data = helper.generate_user_data()

    yield user_data

    data = {
        "email": user_data["email"],
        "password": user_data["password"],
    }
    response = requests.post(urls.LOGIN_USER, json=data)
    token = response.json().get("accessToken")

    if token:
        requests.delete(urls.USER_DATA, headers={'Authorization': token})


@pytest.fixture
def token():
    data = helper.generate_user_data()
    response = requests.post(urls.REGISTER_USER, json=data)
    token = response.json().get("accessToken")

    yield token
    requests.delete(urls.USER_DATA, headers={'Authorization': token})

