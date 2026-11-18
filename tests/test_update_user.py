import allure
from api.user_api import UserApi
from data import BASE_URL
from helpers import generate_random_string

@allure.feature("Изменение данных пользователя")
class TestUpdateUser:
    @allure.title("Изменение данных с авторизацией")
    def test_update_user_with_auth(self, user_credentials):
        api = UserApi(BASE_URL)
        new_name = generate_random_string()
        payload = {"name": new_name}
        response = api.update_user(payload, token=user_credentials["token"])
        assert response.status_code == 200
        assert response.json()["user"]["name"] == new_name

    @allure.title("Изменение данных без авторизации")
    def test_update_user_without_auth(self):
        api = UserApi(BASE_URL)
        payload = {"name": generate_random_string()}
        response = api.update_user(payload)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"