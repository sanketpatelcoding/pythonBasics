class Person:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newname):
        self.__name = newname


p = Person("dedeef")
print(p.getName())

p.setName("bbbbb")
print(p.getName())

p.setName("ram")
print(p.getName())
