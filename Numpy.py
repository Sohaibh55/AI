
import numpy as np
from math import sqrt
# ----------------------------------Seance 1---------------------------------------------

# Numpy - Numeric Python 

# ndarray = n-dimensional array 
# ----------------Rule : numpy.array(object, dtype=None)--------------------
np1 = np.array([0,1,2,3,4,5,6,7])
print(np1)
print(np1.shape)

# Range 
# ----------------Rule : numpy.arange(start, stop, step, dtype=None)--------------------
np2 = np.arange(10)
print(np2)

# Step 
# ----------------Rule : numpy.arange(start, stop, step, dtype=None)--------------------
np3 = np.array([0,1,2,3,4,5,6,7])
np3 = np.arange(2,11,2)
print(np3)

# Zeros
# ----------------Rule : numpy.zeros(shape, dtype=float)--------------------
np4 = np.zeros(10)
print(np4)
# Multidimensional zeros
np5 = np.zeros((2,10))
print(np5)

# Full
# ----------------Rule : numpy.full( (shape) , fill_value, dtype=None)--------------------
np6 = np.full((10),6)
print(np6)
# Multidimensional Full
np7 = np.full((2,10),6)
print(np7)


# ----------------------------------Seance 2---------------------------------------------

# Slicing Numpy Arrays 

np9 = np.array([1,2,3,4,5,6,7,8])
# => return 2,3,4,5
print(np9[1:5])
# => return from something till the end of the array
print(np9[3:]) 
# => return negative slices
print(np9[-7:-1])

# Steps
print(np9[0:8:2])
# Steps on the entire array 
# ---------Rule : array[start:stop:step]---------------
print(np9[::2]) 
print(np9[::3])


# slice a 2 -d array
# ----------------Rule : array[row_index, column_index] or array[row_slice, column_slice]--------------------
np9 = np.array([[1,2,3,4],[6,7,8,9]])
print(np9)

# Pull out a single item and slice 2-d array 

print(np9[0])   # => array[row_index]
print(np9[0,2]) # => array[row_index, column_index]
print(np9[1])
print(np9[1,2])

# slice from both rows
print(np9[0:2 , 1:3]) # 0:2 is the first row to 2 - 1 = 1 row and 1:3 is columns 
print(np9[0,[1,3]])  # array[row_index, [column_indices]]


# ----------------------------------Seance 3---------------------------------------------

# Numpy Universal Function 
np10 = np.array([0,1,-2,3,4,5,6,7,8])
print(np1)
# square route of each element 
print(np.sqrt(np10))

# Absolute Value ;
print(np.absolute(np10)) # like abs in c++

# Exponents
print(np.exp(np10))

# Max and Min
print(np.min(np10))
print(np.max(np10))

# Sign negative or positive 
print(np.sign(np10)) # if number is negative return -1 else return 1 else 0

# Trig sin cos log
print(np.log(np10))

# ----------------------------------Seance 4---------------------------------------------
# Copy Vs. View  1- view => If you modify the view, the original array will also be modified, and vice versa. 
#                   Copy => If you modify the copy, the original array will not be affected, and vice versa.
np11 = np.array([0,1,2,3,4,5,6,7,8,9,10])

# Create a view 
np12 = np11.view() 
np13 = np11.copy() 
print(f'Original NP11 {np11}')
print(f'Original NP12 {np12}')
print(f'Original NP13 {np13}')

np11[0] = 11

print(f'\n after modified : np11[0] = 11 , np12[1] = 12 , np13[2] = 13 \n')
print(f'Changed NP11 {np11}')
print(f'Changed NP12 {np12}')
print(f'Not changed  NP13 {np13}')
 