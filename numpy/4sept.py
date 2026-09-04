"""
1.Create an array of 10 student marks using np.array().
2.Generate even numbers from 2 to 50 using np.arange().
3.Create 8 equally spaced values from 100 to 500 using np.linspace().
4.Create a 4*4 matrix of zeros.
5.Create a 5*5 identity matrix.
6.Generate 20 random marks between 35 and 100.
7.Select 3 random fruits using np.random.choice().
8.Use np.random.seed(50) and generate 10 random integers between 1 and 100. Compare the output by running the code twice.
"""
import numpy as np

# statistics : 

"""
arr =np.array([1,34,56,23,11,89,90])
print(arr.mean())  # mean of the array  : total sum / total number of elements  : 35.66
print(arr.var())  # variance of the array  : total sum of squares / total number of elements - mean of the array
print(arr.std())  # standard deviation of the array  : square root of variance of the array

print(np.median(arr))  # middle value of the array  : 

# [1,11,23,34,56,89,90]   # sort  : (23 +34) /2  size ----> even   ====> n1+n2 /2 
"""

# np.floor  :  only for integers

"""
arr =np.array([12.34 ,67.89,23.01,45.44])
print(np.floor(arr))  # floor of the array  
"""
# np.ceil  :  round up to the next integer
"""arr =np.array([12.34 ,67.89,23.00,45.44])
print(np.ceil(arr))  # ceil of the array
"""

# log : 
"""arr =np.array([2,3,5,9,10])

print(np.log(arr))
print(np.log10(arr))
"""

# np.sin ,np.cos ,np.tan : 

arr =np.array([2,3,5,9,10])
print(np.sin(arr))
