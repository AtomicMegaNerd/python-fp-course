from typing import Optional
from fp.customer import Customer


class Order:
    # class attribute
    orders: list = []

    # instance attributes
    orderid: int = 0
    shipping_address: str = ""
    expedited: bool = False
    shipped: bool = False
    customer: Optional[Customer] = None

    @staticmethod
    def test_expedited(order):
        return order.expedited

    @staticmethod
    def test_shipped(order):
        return order.shipped

    @staticmethod
    def get_customer_name(order):
        return order.customer.name

    @staticmethod
    def get_customer_address(order):
        return order.customer.address

    @staticmethod
    def get_shipping_address(order):
        return order.shipping_address

    @staticmethod
    def get_filtered_orders_customer_names(predicate, get_property):
        return map(get_property, filter(predicate, Order.orders))

    @staticmethod
    def get_expedited_orders_customer_names():
        return Order.get_filtered_orders_customer_names(
            Order.test_expedited, Order.get_customer_name
        )

    @staticmethod
    def get_expedited_orders_customer_addresses():
        return Order.get_filtered_orders_customer_names(
            Order.test_expedited, Order.get_customer_address
        )

    @staticmethod
    def get_expedited_orders_shipping_addresses():
        return Order.get_filtered_orders_customer_names(
            Order.test_expedited, Order.get_shipping_address
        )
