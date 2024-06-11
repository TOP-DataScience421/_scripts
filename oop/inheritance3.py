class Vehicle:
    wheels: int
    
    def __init__(self, speed):
        self.speed = speed
    
    @staticmethod
    def move():
        print(f'{self.__class__.__name__} движется по земле со скоростью {self.speed} км/ч')


class Bicycle(Vehicle):
    wheels = 2


class Car(Vehicle):
    wheels = 4
    
    @staticmethod
    def move():
        print(f'{self.__class__.__name__} движется по дороге со скоростью {self.speed} км/ч')


# пример неоднозначного наследования
class Train(Vehicle):
    wheels = 12
    
    @staticmethod
    def move():
        print(f'{self.__class__.__name__} движется по рельсам со скоростью {self.speed} км/ч')


# пример некорректного наследования
class Aircraft(Vehicle):
    wheels = 6
    
    def __init__(self, ground_speed, air_speed):
        self.ground_speed = ground_speed
        self.air_speed = air_speed
    
    @staticmethod
    def move():
        print(f'{self.__class__.__name__} движется по земле со скоростью {self.ground_speed} км/ч и в воздухе со скоростью {self.air_speed} км/ч')


vehicles = (
    Car(70),
    Bicycle(16),
    Car(90),
    Train(110),
    Aircraft(50, 500)
)

for vehicle in vehicles:
    print(f'{vehicle.speed = }')

