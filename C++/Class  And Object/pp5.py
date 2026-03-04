class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"{self.brand} accelerated to {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        print(f"{self.brand} slowed down to {self.speed} km/h")

car1 = Car("Toyota", 60)
car1.accelerate()  # Output: Toyota accelerated to 70 km/h
car1.brake()       # Output: Toyota slowed down to 60 km/h

car2 = Car("Honda", 80)
car2.accelerate()  # Output: Honda accelerated to 90 km/h
car2.brake()       # Output: Honda slowed down to 80 km/h