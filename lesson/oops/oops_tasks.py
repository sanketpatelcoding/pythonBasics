class Person:
    def __init__(self, name, age,city):
        self.name = name
        self.age = age
        self.city = city
    def showinfo(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"age: {self.age}")
        print(f"city: {self.city}")
    # my method
    def greet(self):
        print("Hellod greeting!")
person1 = Person("sanket", 30,'gnagar')
person1.showinfo()
person1.greet()

