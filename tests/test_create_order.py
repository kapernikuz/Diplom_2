import allure
from api.order_api import OrderApi
from data import BASE_URL

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth_and_ingredients(self, user_credentials):
        api = OrderApi(BASE_URL)
        ingredients_response = api.get_ingredients()
        ingredient_ids = [ing["_id"] for ing in ingredients_response.json()["data"]][:2]
        
        payload = {"ingredients": ingredient_ids}
        response = api.create_order(payload, token=user_credentials["token"])
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, user_credentials):
        api = OrderApi(BASE_URL)
        payload = {"ingredients": []}
        response = api.create_order(payload, token=user_credentials["token"])
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredient_hash(self, user_credentials):
        api = OrderApi(BASE_URL)
        payload = {"ingredients": ["invalid_hash_123", "another_invalid_hash"]}
        response = api.create_order(payload, token=user_credentials["token"])
        assert response.status_code == 500