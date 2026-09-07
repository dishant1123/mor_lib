import  numpy as np 

#slicing  : 
"""
index start  : 0 1 2,3 ....  -----> l to r 
neg index : r to  l  -----> -1 -2 -3 

"""
"""arr =np.array([12,34,56,78,134,57,90])
#              0  1   2  3  4  5  6 
#            -6    -5   -4   -3   -2  -1 
print(arr[3]) # 78 
print(arr[3:5]) # 78 134 
print(arr[-1])  # 0 
print(arr[2 :6 :3])  # start 2 stop  6 step 3  ---> 56 57 

print(arr[-2 :-5 :-1 ])  # start  : -2 end  -5 
print(arr[-5 :-2 ])  # start  : -5 end  -2 

# s ---> 57 134 78 56 

print(arr[ : : -2])
print(arr[ :  : ])
print(arr[ : : -1 ])
"""

# slicing  with 2d array  : 

arr =np.array([
    [1,2,3,4,5],        # 0
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])
print(arr[2:5]) # first row  slincing  , sec col slincing
print(arr[ :, 2:5 ])
print(arr[1:4,2:4 ])  # row slicing  :1:4 , col slicing :2:4
print(arr[1:4:2, : 4:2])
print(arr[ : 5 :3 , : : -3])
"""
[1,2,3,4,5],        #  row first  : 0
[6,7,8,9,10],       #     sec     :1  
[11,12,13,14,15],   #     third   :2
[16,17,18,19,20],   #     fourth  :3
[21,22,23,24,25]    #     fifth   :4
col  : 
1 6  11 16  21 ---->  0 
2 7  12 17  22 ---->  1 
3 8  13 18  23 ---->  2 
4 9  14 19  24 ---->  3 
5 10 15 20  25 ---->  4


[1,2,3,4,5], # 5 2
[16,17,18,19,20],   #     fourth  20 17
"""
