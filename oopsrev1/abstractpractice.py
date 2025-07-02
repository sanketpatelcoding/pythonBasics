from abc import ABC, abstractmethod



class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


d = Dog().make_sound()
c = Cat().make_sound()
print(d)
print(c)