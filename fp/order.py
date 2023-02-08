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
    order_items: list

    def __init__(
        self, orderid, shipping_address, expedited, shipped, customer, order_items
    ) -> None:
        self.orderid = orderid
        self.shipping_address = shipping_address
        self.expedited = expedited
        self.shipped = shipped
        self.customer = customer
        self.order_items = order_items

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
    def filter(predicate, it):
        return list(filter(predicate, it))

    @staticmethod
    def map(func, it):
        return list(map(func, it))

    @staticmethod
    def get_filtered_info(predicate, get_property, orders):
        return Order.map(get_property, Order.filter(predicate, orders))

    @staticmethod
    def get_expedited_orders_customer_names():
        return Order.get_filtered_info(
            Order.test_expedited, Order.get_customer_name, Order.orders
        )

    @staticmethod
    def get_expedited_orders_customer_addresses():
        return Order.get_filtered_info(
            Order.test_expedited, Order.get_customer_address, Order.orders
        )

    @staticmethod
    def get_expedited_orders_shipping_addresses():
        return Order.get_filtered_info(
            Order.test_expedited, Order.get_shipping_address, Order.orders
        )

    @staticmethod
    def set_order_expedited(orderid, orders):
        for order in Order.get_order_by_id(orderid, orders):
            order.expedited = True

    @staticmethod
    def get_order_by_id(orderid, orders):
        return Order.filter(lambda o: o.orderid == orderid, orders)

    @staticmethod
    def notify_backordered(orders, msg):
        Order.get_filtered_info(
            lambda o: any(i.notify_backordered for i in o.order_items),
            lambda o: o.customer.notify(o.customer, msg),
            orders,
        )
