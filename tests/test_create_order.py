import allure
import requests
import urls
from data import Ingredients
from data import ErrorMessages


@allure.feature('Проверяем создание заказа')
class TestApiCreateOrder:
    @allure.title('Создание заказа с ингредиентами для авторизованного пользователя')
    def test_auth_user_create_order_successful(self, token):
        user_token = token
        data = Ingredients.INGREDIENTS
        response = requests.post(urls.ORDER, headers={'Authorization': user_token}, json=data)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_with_ingredients_user_no_auth_successful(self):
        data = Ingredients.INGREDIENTS
        response = requests.post(urls.ORDER, json=data)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients_error(self):
        data = Ingredients.WITHOUT_INGREDIENTS
        response = requests.post(urls.ORDER, json=data)
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessages.INGREDIENT_ERROR

    @allure.title('Создание заказа с некорректными ингредиентами')
    def test_create_order_bad_ingredients_error(self):
        data = Ingredients.INVALID_HASH_INGREDIENTS
        response = requests.post(urls.ORDER, json=data)
        assert response.status_code == 500
        assert ErrorMessages.SERVER_ERROR in response.text

