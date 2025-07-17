class Bird:
    def move(self):
        return 'i am a bird'


class Mammal:
    def move1(self):
        return 'no eggs'

class Bat(Bird, Mammal):
    def mychar(self):
        return f"bat say: {self.move()}, i dont have : {self.move1()}"

bat1 = Bat()
print(bat1.mychar())