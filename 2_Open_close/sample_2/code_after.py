"""
The solution for the PaymentGateway and Order classes was to inject the PaymentGateway object
into the Order class as a dependency, rather than instantiating it inside the process_order() method.

This way, the Order class is open for extension because it can use any payment gateway object
that adheres to a common interface, without needing to modify the Order class itself.
"""


class PaymentGateway:
    def process_payment(self, amount):
        # code to process payment
        pass


class Order:
    def __init__(self, amount, gateway):
        self.amount = amount
        self.gateway = gateway

    def process_order(self):
        self.gateway.process_payment(self.amount)


if __name__ == '__main__':
    gateway = PaymentGateway()
    order = Order(100, gateway)
    order.process_order()
