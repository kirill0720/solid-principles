"""
The PaymentGateway and Order classes violate the Open-Closed Principle
because the Order class is tightly coupled to the PaymentGateway class.

If a new payment gateway is added in the future, the Order class would need to be modified
to use the new gateway, breaking the principle of being closed for modification.
"""


class PaymentGateway:
    def process_payment(self, amount):
        # code to process payment
        pass


class Order:
    def __init__(self, amount):
        self.amount = amount

    def process_order(self):
        gateway = PaymentGateway()
        gateway.process_payment(self.amount)


if __name__ == '__main__':
    order = Order(100)
    order.process_order()
