import pytest
import requests
import helper
import urls


@pytest.fixture(scope='function')
def user():
    data = helper.generate_user_data()
    response = requests.post(urls.REGISTER_USER, data=data)
    token = response.json()['accessToken']
    yield response, data
    requests.delete(urls.USER_DATA, headers={"Authorization": f'{token}'})


