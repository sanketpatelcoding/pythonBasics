# uname=str(input("enter username:"))
# pword=str(input("enter password:"))
#
# if(uname=='user'and pword=='user1'):
#     print('you are logged in')
# else:
#     print('wrong credentials')

cred = {'uname': 'one', 'pword': 'two'}


input_uname = input("Enter username: ")
input_pword = input("Enter password: ")


if (input_uname == cred['uname'] and input_pword == cred['pword']):
    print("Loggedin")
else:
    print("Wrong credentials.")
