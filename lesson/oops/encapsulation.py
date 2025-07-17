class Person:
    def __init__(self, name):
        self.name = name
    def show_info(self):
        print(f"name: {self.name}")

class Employee(Person):
    def __init__(self, name, empid):
        super().__init__(name)
        self._employee_id = empid

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, a):
        self._employee_id = a

    def get_employee_info(self):
        print(f"name is: {self.name}")
        print(f"emp id: {self._employee_id}")
emp1 = Employee("Sanket", 30)

emp1.get_employee_info()

print(" getter:", emp1.get_employee_id())
emp1.set_employee_id("ddfd")
print(f"new id:{emp1.get_employee_info()}")

