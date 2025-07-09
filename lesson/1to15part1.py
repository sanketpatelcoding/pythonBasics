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
numbers = [10, 25, 15, 40, 30]

def funx(list):
    largest = second = list[0]
    # setting both to first element
    for num in list:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

print("Second largest is:", funx(numbers))


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







