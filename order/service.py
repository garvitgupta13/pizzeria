import random
import string
import time


class OrderService:
    """
    Service layer to handle orders
    """

    @classmethod
    def create_order(cls, order_id: str):
        """
        Creates order

        :param order_id: Order ID
        """
        print(f"Creating order : {order_id}")
        time.sleep(2)
        print(f"Created order {order_id} successfully")

    @classmethod
    def generate_order_id(cls) -> str:
        """
        Generate order id

        :return: Order id (String of 7 random characters)
        """
        return "".join(random.choices(string.ascii_uppercase, k=7))
