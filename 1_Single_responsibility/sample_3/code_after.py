"""
The solution was to separate the responsibility of servicing the car into a separate CarService class.
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


class CarService:
    def service(self, car):
        # Code to service car
        pass
