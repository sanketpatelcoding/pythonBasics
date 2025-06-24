class fruit:
    def fruitcon(self):
        print('i am a fruit calss')

class mango(fruit):
    def mangocon(self):
        print('i am amngo class')

class kesar(mango):
    def kesar(self):
        print('i am kesar')


kesarObj=kesar()
kesarObj.kesar()
kesarObj.mangocon()
kesarObj.fruitcon()

