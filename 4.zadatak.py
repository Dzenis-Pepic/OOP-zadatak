class Vehicle:
    def __init__(self,max_speed,mileage,capacity):
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity
    def seating_capacity(self):
        return self.capacity

class Bus(Vehicle):
    def __init__(self,max_speed,mileage,capacity=50):
        super().__init__(max_speed,mileage,capacity)
