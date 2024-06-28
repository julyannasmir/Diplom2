import allure
import requests
import urls
from data import ErrorMessages


@allure.feature('Получение заказа пользователя')
class TestApiGetUserOrders:
    @allure.title('Получение заказа авторизованного пользователя')
    def test_get_auth_user_order(self, token):
        user_token = token
        response = requests.get(urls.ORDER, headers={'Authorization': user_token})
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Получение заказа пользователя без авторизации')
    def test_get_user_order_without_auth(self):
        user_token = None
        response = requests.get(urls.ORDER, headers={'Authorization': user_token})
        assert response.status_code == 401
        assert ErrorMessages.UNAUTHORIZED in response.text


