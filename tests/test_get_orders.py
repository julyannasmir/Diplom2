import allure
import requests
import urls
from data import ErrorMessages


@allure.feature('Получение заказа пользователя')
class TestApiGetUserOrders:
    @allure.title('Получение заказа авторизованного пользователя')
    def test_get_auth_user_order(self, user):
        token = user[0].json()['accessToken']
        response = requests.get(urls.ORDER, headers={'Authorization': token})
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Получение заказа пользователя без авторизации')
    def test_get_user_order_without_auth(self):
        response = requests.get(urls.ORDER, headers={'Authorization': None})
        assert response.status_code == 401
        assert ErrorMessages.UNAUTHORIZED in response.text


