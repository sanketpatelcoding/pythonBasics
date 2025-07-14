# Write a function to reverse a string in Python.
# def reverse_string():
#     s = input("Enter a string: ")
#     print("Reversed string:", s[::-1])
#
# reverse_string()
# without using inbuilt
# def reversestring():
#     s = input("Enter a string: ")
#     reversedstr = ""
#     for char in s:
#         reversedstr = char + reversedstr
#     print("Reversed string:", reversedstr)
#
# reversestring()

#----------------------------------------------
# 2 Create a function to find the maximum element in a list.

# numbers = [4, 2, 9, 1, 7]
# maximum = max(numbers)
# print("Maximum:", maximum)

# without inbuilt function
# mylist = [8, 15, 3, 27, 6]
# def findmax(l1):
#     maxnum = l1[0]
#     for num in l1:
#         if num > maxnum:
#             maxnum = num
#     return maxnum
# print("biggest number is:", findmax(mylist))

# ------------------------------------------------------

# 4 Write a function to remove duplicate elements from a list.

# my_list = [1, 4,4,4,4]
# def removeduplicates(lst):
#     result = []
#     for item in lst:
#         if item not in result:
#             result.append(item)
#     return result
#
# new_list = removeduplicates(my_list)
# print("after removing :", new_list)

# -----------------------------------------------------

# 7 Write a function to find the sum of all numbers in a list.

# a = [1,3,4,5,6,6]
# def findsum(lst):
#     sum = 0
#     for num in lst:
#         sum = sum+num
#     return sum
#
# print("Sum of numbers:", findsum(a))

# ----------------------------------------------------------

# 9.Create a function to convert temperature from Celsius to Fahrenheit.
# def c2f(cel):
#     f = (cel * 9/5) + 32
#     return f
# tempinc = float(input("Enter the temperature in cel: "))
# print(f"tems in cels is: {tempinc}")
#
# tempinf = c2f(tempinc)
# print("Temp in faren:", tempinf)

# ----------------------------------------------------
# 11 Implement a function to find the second largest element in a list.
# (with internet help)
# numbers = [10, 25, 15, 40, 30]
#
# def funx(list):
#     largest = second = list[0]
#     # setting both to first element
#     for num in list:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num
#     return second
#
# print("Second largest is:", funx(numbers))
#

# ---------------------------------------------

# 8.	Implement a function to sort a list of numbers in ascending order.

# lst = [5, 2, 8]
# print(len(lst))  # Output: 3
# using len concept
# numbers = [4, 1, 3, 2]

#
# def a(l):
#     for i in range(len(l)):
#         for j in range(i + 1, len(l)):
#             if l[i] > l[j]:
#                 l[i], l[j] = l[j], l[i]
#     return lst
#
# print("asc order:", a(numbers))

# =================================================

# 6.Factorial of a number
# def factorial(n):
#     a = 1
#     for i in range(1, n + 1):
#         a *= i
#     return a
#
# n = int(input("Enter a number to find factorial"))
# print(f'Factorial  is {factorial(n)}')

# ------------------------------------

# 1 prime number or not
#
# def checkp(n):
#     if n <= 1 and n==0:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# n = int(input("Enter  number"))
# if checkp(n):
#     print(f"{n} is prime .")
# else:
#     print(f"{n} not a prime.")

# -------------------------------
# 4/duplicate remove from list
# def removeduplicate(l1):
#     result = []
#     for item in l1:
#         if item not in result:
#             result.append(item)
#     return result
# l1 = [1, 2, 3, 2, 4]
# print(removeduplicate(l1))

# -------------------------------------
# 5/ check 4 palindrome series
# not working propoerly for spqce
# def palind(s):
#     return s == s[::-1]
#
# s = input('Enter a string')
# if palind(s):
#     print(' palindrome.')
# else:
#     print('not a palindrome.')

# -------------------------------------
# 10 fibonacci series generate
# def f(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
#
# n = int(input("Enter number: "))
# f(n)


# ===============================
# 12.       vowel


# def countvowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#
#             count += 1
#     return count
# s = input('Enter string')
# print("Number of vowels", countvowels(s))

# -----------------------
#(from internet)
# def anag(str1, str2):
#     return sorted(str1) == sorted(str2)
# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
#
# if anag(s1, s2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")
# =======================================

#14 Implement a function to find the intersection of two lists.

def f(l1, l2):
    result = []
    for item in l1:
        if item in l2 and item not in result:
            result.append(item)
    return result
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

print(f' this is{f(l1, l2)}')







