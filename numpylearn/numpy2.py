import numpy as np

# 1 idagonal matrix.identity matrix
# x=np.eye(2,4)
# print(x)
# ------------------------------------
#2. get the dimension
# a=np.array(5)
# b=np.array([1,2,3])
# c=np.array([[1,2,3],[4,5,6]])
# print(c.ndim)
# ...........................................
#pow
# base=np.array([2,3,4])
# exp=np.array([2,2,2])
# result=pow(base,exp)
# print(result)
# ................................................

# clip to limit values in range
# a=np.array([[1,2,3,4,5,6],[1,4,3,5,6,8]])
# b=np.clip(a,3,7)
# print(b)

# ravel
# x = np.array([[1, 2, 3], [4, 5, 6]])
# np.ravel(x)
# print(x)

# ----------------------
# nan_to_num
# :NaN (Not a Number):  undefined or unrepresentable values, like the result of 0/0.
# inf (Infinity):  positive infinity, like 1/0.
# -inf (Negative Infinity):  negative infinity-1/0.
# arr = np.array([1.0, np.nan, np.inf, -np.inf, 5.0])
# print(arr)
# result = np.nan_to_num(arr, nan=1, posinf=4, neginf=-4)
# result=np.nan_to_num(arr)
# print(result)

#======================================


# numpy.isnan:
#
# Checks which elements in an array are NaN.
# Return a boolean array (True for NaN, False otherwise).
# arr = np.array([1.0, np.nan, 3.0, np.nan])
# # arr = np.array([1.0, 0/0 , 3.0,0/0 ]) (not working ask ?)
# is_nan = np.isnan(arr)
# print(is_nan)

# -------------------------------------------

# np.where

# arr = np.array([1.0, np.nan, np.inf, 5.0])
# # change NaN with 0, keep other values unchanged
# result = np.where(np.isnan(arr), 0, arr)
# print(result)

# ---------------------------------------------



