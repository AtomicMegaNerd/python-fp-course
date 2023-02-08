"""
The customer is always right
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    """
    A Customer class
    """

    name: str = ""
    address: str = ""
    enterprise: bool = False

    @staticmethod
    def notify(cust, msg):
        """
        notify the customer.
        """
        print(f"Sending {msg} to {cust.name} at {cust.address}")
