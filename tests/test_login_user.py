import allure
from api.user_api import UserApi
from data import BASE_URL
from helpers import generate_random_email, generate_random_string

@allure.feature("Логин пользователя")
class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, user_credentials):
        api = UserApi(BASE_URL)
        payload = {
            "email": user_credentials["email"],
            "password": user_credentials["password"]
        }
        response = api.login(payload)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным логином и паролем")
    def test_login_invalid_credentials(self):
        api = UserApi(BASE_URL)
        payload = {
            "email": generate_random_email(),
            "password": generate_random_string()
        }
        response = api.login(payload)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"