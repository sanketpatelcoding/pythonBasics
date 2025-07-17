class Person:
    def __init__(self, name):
        self.name = name
    def details(self):
        print(f"Name: {self.name}")
class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
    def get_employee_info(self):
        print(f"Name: {self.name}")
        print(f"emp id: {self.employee_id}")
emp1 = Employee("Sanket", 30, )

emp1.details()
emp1.get_employee_info()
