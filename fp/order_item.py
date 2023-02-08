"""
OrderItem
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderItem:
    """
    Stores items in an order
    """

    name: str
    itemnumber: int
    quantity: int
    price: float
    backorderd: bool
