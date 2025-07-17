
from abc import ABC, abstractmethod
# ABC : Abstract Base Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        return 'engine started'

    

class Car(Vehicle):
    def start(self):
        return '4wheelerstatr'

class Motorcycle(Vehicle):
    def start(self):
        return 'bulletstatr'

car=Car()
mc=Motorcycle()
vehicles = [car,mc]
for vehicle in vehicles:
    print(vehicle.start())
#
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
#
# voice(animal)
# voice(dog)
# voice(cat)