import allure
import requests
import urls
from data import ErrorMessages


@allure.feature('Проверка изменения данных пользователя')
class TestApiUpdateUserData:
    @allure.title('Успешное изменение почты пользователя')
    def test_change_user_email(self, user):
        token = user[0].json()['accessToken']
        modify_data = {"email": 'super random email'}
        response = requests.patch(urls.USER_DATA, headers={'Authorization': token}, json=modify_data)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Успешное изменение пароля пользователя')
    def test_change_user_password(self, user):
        token = user[0].json()['accessToken']
        modify_data = {"password": 'random password'}
        response = requests.patch(urls.USER_DATA, headers={'Authorization': token}, json=modify_data)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Успешное изменение имени пользователя')
    def test_change_user_name(self, user):
        token = user[0].json()['accessToken']
        modify_data = {"name": 'random name'}
        response = requests.patch(urls.USER_DATA, headers={'Authorization': token}, json=modify_data)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Изменение почты пользователя без авторизации')
    def test_change_user_email_without_auth(self):
        modify_data = {"email": 'random email'}
        response = requests.patch(urls.USER_DATA, json=modify_data)
        assert response.status_code == 401
        assert ErrorMessages.UNAUTHORIZED in response.text

    @allure.title('Изменение пароля пользователя без авторизации')
    def test_change_user_password_without_auth(self):
        modify_data = {"password": 'random password'}
        response = requests.patch(urls.USER_DATA, json=modify_data)
        assert response.status_code == 401
        assert ErrorMessages.UNAUTHORIZED in response.text

    @allure.title('Изменение имени пользователя без авторизации')
    def test_change_user_name_without_auth(self):
        modify_data = {"name": 'random name'}
        response = requests.patch(urls.USER_DATA, json=modify_data)
        assert response.status_code == 401
        assert ErrorMessages.UNAUTHORIZED in response.text

