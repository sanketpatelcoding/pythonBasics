class Employee:
    def __init__(self):
        self.__empid = None

    def getemp_id(self):
        return self.__empid

    def setemp_id(self,empid):
        self.__empid=empid


emp = Employee()
emp.setemp_id('1')
print(f'emp id is{emp.getemp_id()}')

