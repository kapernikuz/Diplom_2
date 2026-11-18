import allure
from api.user_api import UserApi
from data import BASE_URL
from helpers import generate_random_email, generate_random_string

@allure.feature("Создание пользователя")
class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, cleanup_user):
        api = UserApi(BASE_URL)
        payload = {
            "email": generate_random_email(),
            "password": generate_random_string(),
            "name": generate_random_string()
        }
        response = api.register(payload)
        
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

        
        token = response.json().get("accessToken")
        cleanup_user.append(token)

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, user_credentials):
        api = UserApi(BASE_URL)
        payload = {
            "email": user_credentials["email"],
            "password": user_credentials["password"],
            "name": user_credentials["name"]
        }
        response = api.register(payload)
        
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_missing_field(self):
        api = UserApi(BASE_URL)
        payload = {"email": generate_random_email(), "password": generate_random_string()} # Нет name
        response = api.register(payload)
        
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"