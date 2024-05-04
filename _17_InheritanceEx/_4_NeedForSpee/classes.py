class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        consumption = kilometers * self.fuel_consumption

        temp = self.fuel - consumption

        if temp >= 0:
            self.fuel = temp


class Motorcycle(Vehicle):
    pass


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8


class CrossMotorcycle(Motorcycle):
    pass


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3


class FamilyCar(Car):
    pass


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
