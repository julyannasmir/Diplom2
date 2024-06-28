import allure
import requests
import urls
from data import ErrorMessages


@allure.feature('Проверка авторизации пользователя')
class TestLoginUser:
    @allure.title('Успешная авторизация')
    def test_login_existing_user(self, user):
        data = user
        requests.post(urls.REGISTER_USER, json=data)
        response_2 = requests.post(urls.LOGIN_USER, json=data)
        assert response_2.status_code == 200 and response_2.json()['success'] is True

    @allure.title('Авторизация с неверным логином')
    def test_login_user_incorrect_email_error(self, user):
        data = user.copy()
        data["email"] = 'new_incorrect_email'
        response = requests.post(urls.LOGIN_USER, json=data)
        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessages.INCORRECT_DATA

    @allure.title('Авторизация с неверным паролем')
    def test_login_user_incorrect_password_error(self, user):
        data = user.copy()
        data["password"] = 'new_incorrect_password'
        response = requests.post(urls.LOGIN_USER, json=data)
        assert response.status_code == 401
        assert response.json()['message'] == ErrorMessages.INCORRECT_DATA

