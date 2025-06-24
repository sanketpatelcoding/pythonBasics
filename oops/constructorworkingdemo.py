class Tata:
    name:'tataGroup'
    regno:1

    def __init__(self):
        print('TATA grp info.-welcome')
    def construct(self,name,regno):
        self.name=name
        self.regno=regno
        print(self.regno,self.name)
#
tatamotor=Tata()
tatamotor.__init__()
tatamotor1=Tata()
print(tatamotor1.construct('tata motors',2))

