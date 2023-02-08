"""
This is where the magic happens
"""
from dataclasses import dataclass
from fp.customer import Customer
from fp.order_item import OrderItem


@dataclass(frozen=True)
class Order:
    """
    This is our order class.
    """

    # instance attributes
    orderid: int
    shipping_address: str
    expedited: bool
    shipped: bool
    customer: Customer
    order_items: list

    # class attribute
    orders: tuple = ()

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

    @staticmethod
    def mark_backordered(orders, orderid, itemnumber):
        return Order.map(
            lambda o: o
            if o.orderid != orderid
            else (
                Order(
                    o.orderid,
                    o.shipping_address,
                    o.expedited,
                    o.shipped,
                    o.customer,
                    Order.map(
                        lambda i: i
                        if i.itemnumber != itemnumber
                        else OrderItem(i.name, i.itemnumber, i.quantity, i.price, True),
                        o.order_items,
                    ),
                )
            ),
            orders,
        )
