"""
python  data type  : 
1.string 
list 
dict 
set 
tuple 


list -----> mutable sequence of heterogenous data types. ----> [] ---> ordered

memory 
slow 

list convert -----> array  ----> numpy 

less memory 
fast  

list : 

l1= [1,2,3,4,5,6,7,8]   -----> access  ----> index  ---->start 0 

"""

# ex :1 

l1 =[[1,2,3],[4,5,6],[7,8,9]] 
#       0      1       2 
#    [1,2,3] 
# print(l1[0][2])  ----->3 
# print(l1)

"""for i in l1 :
    print(i)
"""

# slicing : 

l1= [13,52,83,49,15,36,97,18]

# l1[5] =900
# print(l1)

"""l1.insert(4,9000)
print(l1)
"""
# [13,52,83,49,9000,15,36,97,18]  ----> r k  
"""
l1= [13,52,83,49,15,36,97,18,909]
# pos -----> l to r 
# neg  -----> r to l
print(l1[5])
print(l1[5:8])  # strat index : 5  end index 8 
print(l1[-3])   # 
print(l1[3 : -3])   #  

print(l1[ 2 :5 :2] )  # start index : 2  end index 5  step 2
print(l1[ 0 :8 :3] )  # start index : 0  end index 8  step 3

print(l1[ : : 2 ])  
print(l1[ : : 1 ])  
print(l1[ : : -1 ])  

"""

# pip install numpy

import numpy as  np  

"""arr =np.array([12,45,67,89,34,56,123]) 
print(arr)
print(type(arr))

# note : in  array we store same data type  value. 
print(arr.ndim)
"""
# 2d array : 
"""
arr =np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [23,67,89]
])
print(arr)
print(type(arr))
print(arr.ndim)
print(arr.size)
"""

# 3d array : 
"""
arr =np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [12,45,78]
    ]
])

print(arr)
print(type(arr))
print(arr.ndim)
print(arr.size)

"""
# array arrtibutes : ndim ,size,shape,dtype,itemsize
arr =np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [23,67,89]
])

print(arr)
print(arr.ndim)   # 2  number  dimension
print(arr.size)   # 12   total number of elements
print(arr.shape)  #(4,3)   row  col 
print(arr.dtype)  # int 
print(arr.itemsize) # bytes

