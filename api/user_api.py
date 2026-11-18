import allure
import requests
from api.base_api import BaseApi
from data import API_URL, REGISTER, LOGIN, USER


class UserApi(BaseApi):
    def register(self, payload):
        return self.post(REGISTER, json=payload)

    def login(self, payload):
        return self.post(LOGIN, json=payload)

    def update_user(self, payload, token=None):
        headers = {"Authorization": token} if token else {}
        return self.patch(USER, json=payload, headers=headers)

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        headers = {"Authorization": token}
        return requests.delete(f"{API_URL}{USER}", headers=headers)