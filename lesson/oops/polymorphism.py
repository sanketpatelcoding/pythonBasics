# class Shape:
#     def area(self):
#         return 'shape area'
# class Circle(Shape):
#     def area(self):
#         return 'circle area'
# class Rectangle(Shape):
#     def area(self):
#         return 'rectangle area'
#
# shapes = [Shape(), Circle(), Rectangle()]
# for shape in shapes:
#     print(shape.area())
# above for my reference
class Shape:
    def area(self):
        return 'general area'
class Circle(Shape):
    def area(self):
        return f'circleArea: {3.14 * self.r *self.r}'
class Rectangle(Shape):
    def area(self):
        return f'rectangle area: {self.length * self.width}'

circle = Circle()
circle.r = 5
rectangle = Rectangle()
rectangle.length = 4
rectangle.width = 6
shapes = [circle, rectangle]
for shape in shapes:
    print(shape.area())