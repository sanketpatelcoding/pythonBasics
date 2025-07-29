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


# *********************************************
#
# Random:

# singlerandom = np.random.rand()
# print("one random number:", singlerandom)
# array1d = np.random.rand(5)
# print("1D array:", array1d)
# array2d = np.random.rand(4, 2)
# print("2D array:\n", array2d)

# ==========================================

#np.random.randn(): generates random numbers from a standard normal distribution
# same as above but from given distribution
# --------------------------------------------------

# random integer between 0 and 9
# singlerandom = np.random.randint(10)
# print(singlerandom)
# array1d = np.random.randint(1, 11, size=4)
# print("1d Array:", array1d)
# array2d = np.random.randint(-5, 6, size=(3, 2))
# print("2D array:", array2d)

# ----------------------------------
# np.random.choice(): Random samples from an array.
# arr = [1, 2, 3, 4, 5]
# print(np.random.choice(arr, size=3))
# # without replacement
# print(np.random.choice(arr, size=3, replace=False) )
# -------------------------------------
# Statistical Methods:
# data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,22,24,26,28,30]
# percentiles = np.percentile(data, q=[25, 50, 75])
# print(percentiles)
# =========================================
# data2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# medianalongaxis0 = np.percentile(data2d, q=50, axis=0)
# print(medianalongaxis0)

# =====histogram

# data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
# hist, binedges = np.histogram(data, bins=6)
# print("Histo counts:", hist)
# print("Bin edges:", binedges)

# =========================

# it is in 3 modes
# 1)For mode='valid': Computes correlation only
# where 2 fully overlaps with 1
# For mode='same': Output size matches (not sure with what)len of 1
# with zero-padding where needed.
# For mode='full': Computes correlation for all possible overlaps,
# resulting in len 1+len 2

# -------------------------------correlate
# a = [1, 2, 3, 4]
# v = [0, 1, 0.5]
# second one is genreally a reference/template
# valid = np.correlate(a, v, mode='valid')
# same = np.correlate(a, v, mode='same')
# full = np.correlate(a, v, mode='full')
#
# print("Valid mode:", valid)
# print("Same mode:", same)
# print("Full mode:", full)

# ===============file i/o
# Save the array to a file
# Load the array from the file

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# np.save('a.npy', arr)
# loadedarray = np.load('a.npy')
# print("orignl:\n", arr)
# print("loadign orgnl:", loadedarray)
# np.savetxt(), np.loadtxt()
# np.savetxt('sample.txt',arr)
# print(f'loading from file:{np.loadtxt('sample.txt')}')
# ----------------------------------

# *************************************
# Masked Arrays:
# np.ma.masked_array(): Create a masked array to handle missing or invalid data.
# ************************************
# Create sample data(t)
# Create a mask (True for elements to be masked)
# Create a masked array
# import numpy.ma as ma
# # data = np.array([1, 2, 3, 4, 5])
# data = np.array(['one', 'two', 'three', 'four', 'five'])
# mask = [False, False, False, False, True]
# maskedarray = ma.masked_array(data, mask=mask)
# print("maskedarray:", maskedarray)
# print("data with mask:", maskedarray.data)
# print("only mask:", maskedarray.mask)
# print("fil that with certain:", maskedarray.filled(fill_value=-6))
#====================================================

# ********************************************
# Linear Algebra:
# ------------------------------------------------------
# np.dot(): Dot product of two arrays.
# a=[1,2,3,4]
# b=[5,6,7,8]
# c=np.dot(a,b)
# print(c)
# ========================================================
# np.linalg.inv(): Inverse of a matrix.

# a=[[1,2],[3,4]]
# inva=np.linalg.inv(a)
# print(inva)
# -------------------------------------

# np.linalg.det(): Determinant of a matrix.
# a=[[1,2,3,4],[4,16,25,36],[1,2,3,4],[1,2,3,4]]
# b=np.linalg.det(a)
# print(b)
# To work the determinant- our matrix must be square( 2×2, 3×3, 4×4.).
# -------------------------------------------
# np.linalg.eig(): Eigenvalues and eigenvectors.
# =========================================
# a=[[1,2,3,4],[4,16,25,36],[1,2,3,4],[1,2,3,4]]
# e_val,e_vector=np.linalg.eig(a)
# print(f'values-{e_val} and \n vector{e_vector}')
# ================================================
# *****************************************
# FFT (Fast Fourier Transform):

# steps
# np.fft.fft() converts the time-domain signal to frequency domain.
a=np.linspace(1,2,10)
# print(a)
b=np.fft.fft(a)
print(b)
# np.abs() gives magnitude of each frequency component.(not needed)
#
# np.fft.fftfreq() computes frequency bins.
d=np.fft.fftfreq(2)
print(d)

# np.fft.fft(): Compute the one-dimensional discrete Fourier Transform.
e= np.fft.fft([1,2])
print(e)
# np.fft.ifft(): Compute the inverse of the one-dimensional discrete Fourier Transform.
f= np.fft.ifft([1,2])
print(f)
# *****************************************


