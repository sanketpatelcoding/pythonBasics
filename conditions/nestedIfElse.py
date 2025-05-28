# amount=float(input("enter billing amount: "))
# print("type 1 if prime member else 0")
# member=bool(input("are you a prime memeber(1:yes)(0:No)"))
# if(member):
#     print("customer is primem member.")
# else:
#     print("customer is NOT a prime member")
# if(amount>=5000):
#      if(member==True):
#             print('15% cashback')
#             print(amount*15/100)
#      else:
#             print('11%cashback')
#             print(amount * 11 / 100)
#     elif(5000<amount>=2500):
#         if (member == True):
#             print('10%cashback')
#             print(amount * 10 / 100)
#         else:
#             print('7%cashback')
#             print(amount * 7 / 100)
#     elif(amount<2500):
#         if (member == True):
#             print('5%cashback')
#             print(amount * 5 / 100)
#         else:
#             print('membership free')
#     else:
#          print(amount)

amount = float(input("enter billing amount: "))
print("type 1 if prime member else 0: ")
member =int(input("are you a prime member(1:yes)(0:No)"))

if member==1:
    print("customer is primem member.")
else:
    print("customer is NOT a prime member")

if amount >= 5000:
    if member == 1:
        print('15% cashback')
        print(amount * 15 / 100)
    else:
        print('11% cashback')
        print(amount * 11 / 100)

elif 5000 > amount >= 2500:
    if member == 1:
        print('10% cashback')
        print(amount * 10 / 100)
    else:
        print('7% cashback')
        print(amount * 7 / 100)

elif 500<=amount < 2500:
    if member == 1:
        print('5% cashback')
        print(amount * 5 / 100)
    else:
        print('membership free')

else:
    print(amount)
