import numpy as np

# tuple: (),,,duplicate,order
#
# list:[],append,remove,duplicate,order
#
# set:{},add,remove,no duplicate,no order

# normally
# list_data = [1, 2, 3, 4, 5]
# tuple_data = (6, 7, 8, 9, 10)
# print(list_data, tuple_data)
# print(type(list_data), type(tuple_data))

# single dimesion
# np_list_array = np.array(list_data)
# np_tuple_array = np.array(tuple_data)
# print(np_list_array, np_tuple_array)
# print(type(np_list_array), type(np_tuple_array))

# two diemension
# arr=[[1,2],[4,5]]
# print(arr,type(arr))
# print(f'{np.array(arr),type(np.array(arr))}')

# ---------------------------lesson---------------------------------
# zeros-------------------------------
# np.zeros(): Create an array of zeros.
# print(np.zeros(3))
# print(np.zeros(3,dtype=int))
# print(np.zeros((2,2),dtype=int))

# ones---------------------------------
# np.ones(): Create an array of ones.
# print(np.ones(0))
# print(np.ones((2,3),dtype=float))

# regular linespace array------------
# np.linspace(): Create an array with evenly spaced values.
#
# lsp_arr=np.linspace(1,2,2)
# print(lsp_arr,type(lsp_arr))
#
# Array Operations:
# array.shape: Get the shape of the array.

# 1d
list_data = [1, 2, 3, 4, 5]
print(np.shape(list_data))
print(np.shape(list_data),type(list_data),type(np.shape(list_data)))
# 2d
list_data=[[1,2],[3,4]]
print(np.shape(list_data),type(list_data),type(np.shape(list_data)))
# became list to tuple


