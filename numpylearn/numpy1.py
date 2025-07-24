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
# list_data = [1, 2, 3, 4, 5]
# print(np.shape(list_data))
# print(np.shape(list_data),type(list_data),type(np.shape(list_data)))
# # 2d
# list_data=[[1,2],[3,4]]
# print(np.shape(list_data),type(list_data),type(np.shape(list_data)))
# became list to tuple

# ---------------------------------------------------------
# array.ndim: Get the number of dimensions.
# list_data = [1, 2, 3, 4, 5]
# print(np.ndim(list_data),type(np.ndim(list_data)))
# list_data=[[1,2],[3,4]]
# print(f'now:{np.ndim(list_data),type(np.ndim(list_data))}')
# -------------------------------------------------
# array.dtype: Get the data type of the array.
# tuple_data = (6, 7, 8, 9, 10)
# list_data = [[1, 2, 3, 4]]
# array_data = np.array(tuple_data)
# print(array_data.dtype)
# print(type(array_data.dtype))
# ---------------------------------------------------------


# array.size: Get the total number of elements.

# a=[1,2,3,4,5]
# b=[[1,2,],[3,4],[5,6]]
# c2np=np.array(b)
# print(c2np.shape)
# print(c2np.size)
# # shape returns tuple ,size gives elements in it

# -----------------------------------------------------------

# array.reshape(): Reshape the array.
# a = [1, 2, 3, 4, 5,6]
# b=np.array(a)
# print(f'before :{b}')
# d=(3,2)
# # i defined tuple above  to make it dynamic in future
# c=b.reshape(d)
# print(f'{c}')
# ---------------------------------------------------

# Indexing and Slicing:

# array[index]: Access elements at a specific index.

# a=[11,2,3,4,5,6,7,8,9,0]
# b=np.array(a)
# print(b[0])
# ============================================

# array[start:stop:step]: Slice arrays.
# a=[11,2,3,4,5,6,7,8,9,0]
# b=np.array(a)
# c=b[0:5:1]
# # till 5th element
# print(c)

# -----------------------------------------
# array[condition]: Boolean indexing.

# a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print('orignal')
# print(a)
# cond = (a <=40)
# ar_c = a[cond]
# print("Filtered")
# print(ar_c)

# =================================================

