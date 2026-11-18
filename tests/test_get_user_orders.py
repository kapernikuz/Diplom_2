import allure
from api.order_api import OrderApi
from data import BASE_URL

@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:
    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_authorized(self, user_credentials):
        api = OrderApi(BASE_URL)
        response = api.get_user_orders(token=user_credentials["token"])
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "orders" in response.json()

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_orders_unauthorized(self):
        api = OrderApi(BASE_URL)
        response = api.get_user_orders()
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"