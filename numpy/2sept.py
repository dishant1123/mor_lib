import  numpy as np

# aithematic  : + - * / % // 

"""
a=np.array([
    [1,2,3],
    [7,6,4],
    [5,8,9]
])

b=np.array([
    [11,34,12],
    [23,45,67],
    [89,56,78]
])

print("a original array :\n",a)
print("b original array :\n",b)
print("sum of  two  array is  \n",a+b)  # element wise addition
print("subtraction of  two  array is  \n",a-b)  # element wise subtraction
print("multiplication of  two  array is  \n",a*b)  # element wise multiplication  its not  matrix multiplication
print(" division of  two  array is  \n",a/b)  # element wise division
print("modulus of  two  array is  \n",a%b)  # element wise modulus
print("floor division of  two  array is  \n",a//b)  # element wise floor division

"""

# matrix multiplication : np.matmul ,np.dot , a@b

"""
a=np.array([
    [1,2,3],
    [7,6,4],
    [5,8,9]
])
b=np.array([
    [11,34,12],
    [23,45,67],
    [89,56,78]
])

print("matrix multiplication of  two  array is  \n",np.matmul(a,b))  # matrix multiplication
print("matrix multiplication of  two  array is  \n",np.dot(a,b))  # matrix multiplication
print("matrix multiplication of  two  array is  \n",a@b)  # matrix multiplication
"""

# rowwise and  col wise sum  : 

a=np.array([
    [11,22,23],
    [7, 6,4],
    [5, 8, 9]
])
# print(np.sum(a))  # 11+22+23+7+6+4+5+8+9=
# print(np.sum(a,axis=0))  # col wise sum : 23 36 45 
# print(np.sum(a,axis=1))  # row wise sum   

# print(np.min(a))
# print(np.min(a,axis=0))  # col wise min
# print(np.min(a,axis=1))  # row wise min

# print(np.max(a))
# print(np.max(a,axis=0))  # col wise max
# print(np.max(a,axis=1))  # row wise max

# print(np.argmin(a))  #return the index number of the minimum value
# print(np.argmin(a,axis=0))  # [2,1,1]
# print(np.argmin(a,axis=1))  # [0 2 0]
 
# print(np.argmax(a))  #return the index number of the maximum value  # tisha
# print(np.argmax(a,axis=0))  # [0,0,0]   # mayu 
# print(np.argmax(a,axis=1))  # [2,0,2]   # vansh 

"""a=np.array([
    [11,22,23],
    [7,6,4],
    [5,8,9]
])

print(np.sort(a))
print(np.sort(a,axis=0))  # col wise sort

print(np.argsort(a,axis=0))  # col wise sort
print(np.argsort(a,axis=1))  # row wise sort
"""