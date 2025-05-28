# s1="sanket patel"
# print(s1+"india")
#
# print(s1[:])
# print(s1[0:])
# print(s1,s1[7:89])
# print(s1*2)
# print(s1,s1)
# print(2*s1,3*s1[4:])
# a=1
# print(bool(a)&False)
# print(type(True))
# print(type(False))
# b=0
#
# a=(a&b)
# print(a)
# identity
a=10;b=25;
print(f'a is {a}')
print(f'b is {b}')
print(type (a))
a=True&False
b=True
a=int(a|b)
print(a)


a=10
b=True
b={a:'ad',b:"a","sap1":a,'sap':b} #to check
print(b,type(b))
print(b.values())
print(b.keys())
print(a in b)
# print(10 in b)
print({10: 'ad', True: 'a', 'sap1': 10, 'sap': True}.values() in b.values())
print(a in b.values()) #working
print(a in b.keys())
# print(b in b)
print(True in b)

# a=b
# print(a is  not( not b))
# a=[10,'10',b]
# print(a)
# # membership
# print(("10" in a) | (10 in a))
# # print((b:"a")in b)
# print(b.keys())
# print(b.values())
# print(True in b)
# print(int(True) in b.values())
# print(10 in b)#keycheck
# print('sap1' in b.keys())#keycheck
# print(b in b.values())#value checking
# print('a' in b.values())#value checking