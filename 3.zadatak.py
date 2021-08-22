class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage


class Bus(Vehicle):
    def __init__(self,max_speed,mileage):
        super().__init__(max_speed,mileage)
