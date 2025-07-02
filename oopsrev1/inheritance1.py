class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

        def printname(self):
            print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

studentObj=    Student('sanket','patel')


