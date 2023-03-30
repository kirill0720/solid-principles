"""
The Car class has to many responsibilities, including driving the car, parking the car, and servicing the car.
This violated the SRP.
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        # Code to start engine
        pass

    def stop_engine(self):
        # Code to stop engine
        pass

    def drive(self):
        # Code to drive car
        pass

    def park(self):
        # Code to park car
        pass

    def service(self):
        # Code to service car
        pass
