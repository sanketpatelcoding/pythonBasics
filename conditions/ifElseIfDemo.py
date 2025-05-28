maths=float(input("enter maths score: "))
phy=float(input("enter phy score: "))
che=float(input("enter che score: "))
bio=float(input("enter bio score: "))
eng=float(input("enter eng score: "))
comp=float(input("enter comp score: "))

avr=(maths+phy+che+bio+eng+comp)/6

mark = {
    'Maths': maths,
    'Physics': phy,
    'Chemistry': che,
    'Biology': bio,
    'English': eng,
    'Computer': comp
}
print(mark)
if(avr>=80):
    print('distinction')
elif(80>avr>=60):
    print('first Class')
elif(60>avr>=51):
    print('second calss')
elif(51>avr>=45):
    print('pass class')
else:
    print('failed')