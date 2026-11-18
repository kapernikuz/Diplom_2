import pytest
from api.user_api import UserApi
from data import BASE_URL
from helpers import generate_random_email, generate_random_string

@pytest.fixture
def user_credentials():
    """Создает уникального пользователя для тестов и удаляет его после."""
    api = UserApi(BASE_URL)
    email = generate_random_email()
    password = generate_random_string()
    name = generate_random_string()

    payload = {"email": email, "password": password, "name": name}
    response = api.register(payload)
    
    # Убираем assert, фикстура просто создает данные
    token = response.json().get("accessToken")

    yield {"email": email, "password": password, "name": name, "token": token}

    # Удаляем пользователя после теста (если он был создан)
    if token:
        api.delete_user(token)

@pytest.fixture
def cleanup_user():
    users_to_delete = []
    yield users_to_delete
    api = UserApi(BASE_URL)
    for token in users_to_delete:
        if token:
            api.delete_user(token)