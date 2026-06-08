class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity


class Bus(Vehicle):
    def fare(self):
        amount = self.capacity * 100
        amount += amount * 0.10
        return amount


bus = Bus(50)
print("Total Bus Fare:", bus.fare())