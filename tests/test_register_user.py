import allure
import requests
import urls
from data import ErrorMessages


@allure.feature('Проверка создания пользователя')
class TestApiRegisterUser:
    @allure.title('Создание нового пользователя')
    def test_create_new_user(self, user):
        response = user[0]
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Создание дубликата пользователя')
    def test_create_duplicate_user(self, user):
        data = user[1]
        response_2 = requests.post(urls.REGISTER_USER, json=data)
        assert response_2.status_code == 403
        assert response_2.json()['message'] == ErrorMessages.ALREADY_EXIST_USER

    @allure.title('Создание пользователя без обязательного поля')
    def test_create_user_without_password(self, user):
        data = user[1]
        data_without_password = {"email": data["email"], "name": data["name"]}
        response = requests.post(urls.REGISTER_USER, json=data_without_password)
        assert response.status_code == 403
        assert response.json()['message'] == ErrorMessages.REQUIRED_FIELDS

