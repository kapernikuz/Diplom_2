from api.base_api import BaseApi
from data import ORDERS, INGREDIENTS

class OrderApi(BaseApi):
    def create_order(self, payload, token=None):
        headers = {"Authorization": token} if token else {}
        return self.post(ORDERS, json=payload, headers=headers)

    def get_user_orders(self, token=None):
        headers = {"Authorization": token} if token else {}
        return self.get(ORDERS, headers=headers)

    def get_ingredients(self):
        return self.get(INGREDIENTS)