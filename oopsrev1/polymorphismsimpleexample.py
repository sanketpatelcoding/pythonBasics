# online reference polymorphism

class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Rectangle:
    def area(self):
        return 4 * 6

def print_area(shape):
    print("Area:", shape.area())


c = Circle()
r = Rectangle()

print_area(c)
print_area(r)