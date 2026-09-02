# np.arange , reshape . np.ones , np.zeros , np.full , np.eye , np.identity , np.diagonal , np.tril , np.triu , np.diag , np.trace , np.transpose  : 

import numpy as np

# arange ,reshape :
"""
arr = np.arange(1,10)  # start stop step 
arr = np.arange(1,10,2)  # start stop step 

arr = np.arange(1,10).reshape(3,3)  
arr =np.arange(1,33).reshape(8,4)
arr =np.arange(1,33).reshape(2,2,2,4)

print(arr)
"""
# np.ones , np.zeros : 

"""arr = np.ones(9,dtype=int)  # by default dtype is float
arr =np.ones((4,4),dtype=int)
print(arr)

arr = np.zeros(9,dtype=int)  # by default dtype is float
arr =np.zeros((4,4),dtype=int)
print(arr)
"""

# np.full :

"""arr =np.full(9,fill_value=99,dtype=int)  # by default dtype is float
arr =np.full((3,4),fill_value=99,dtype=int)  # by default dtype is float

print(arr)
"""

# np.eye : identity  matrix  

"""
ex : 

1 2 3  (0,0)1  (0,1)2  (0,2)3
4 5 6  (1,0)4  (1,1)5  (1,2)6
7 8 9  (2,0)7  (2,1)8  (2,2)9

""" 

"""arr = np.eye(3)
arr = np.eye(4)
arr = np.eye(3,4)
arr =np.identity(3)
print(arr)
"""

# np.transpose :

"""arr =np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("original array :\n",arr)

# trans_arr = np.transpose(arr)
trans_arr = arr.T
print("transpose array :\n",trans_arr)
"""
# np.linespace  : 

"""arr = np.linspace(1,20,3)
print(arr)
"""
# formula  of line space :
"""
stop -start / step -1   -----> 20 - 1 /3-1   = 9.5
"""

# random  : 

import random  
"""
r = random.random()  # value between 0 and 1   -----> 1 excluded 
r=random.randrange(1,20)  # value between 1 and 20  -----> 20 excluded
r=random.randint(1,10)  # value between 1 and 20  -----> both point are included 
print(r)
"""

# array  generate  using  random  module  : 

# arr =np.random.random((3,3))
# arr =np.random.randint(low =-10, high =10, size =(3,3))
# arr =np.random.rand(4,3)

arr2 =np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

np.random.seed(10)
arr=np.random.randint(0,10,(3,3))
print(arr)

