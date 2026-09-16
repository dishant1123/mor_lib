# loadtxt :
"""
1. clean data read  -----> missing  data  not  read
2. nummeric data  / value  read 
"""

import numpy as np

"""
numpy_file  =np.loadtxt("numpy/students.txt",skiprows=1,dtype=int)
print(numpy_file)
"""
# mean  median   : 

"""m = np.mean(numpy_file)
print(m)
me= np.median(numpy_file)
print(me)
le =len(numpy_file)
print(le)

mat = numpy_file.reshape(3,2)
print(mat)

"""
# genfrom txt :
"""
1. read all the  data  also  you can read missing  value  and also fill the  value . 

"""
"""
student = np.genfromtxt("numpy/students2.txt",skip_header=1,delimiter=",",dtype=None,filling_values=23)
print(student)
"""

# np.unique : remove the duplicate  value from array  

"""
arr = np.array([1,2,2,3,3,4,4,5,6,7,8,8,9])

print("original array :",arr)
unique_arr = np.unique(arr)
print("unique array :",unique_arr)
"""


# np.count_nonzero : count the number of non-zero  value in array

arr = np.array([1,2,2,3,3,4,4,5,6,7,8,8,9,0,np.nan,np.nan])
print("original array :",arr)
print("length of array  is : ",len(arr))
num_count = np.count_nonzero(arr)
print("number of non-zero value :",num_count)

# boardcasting :

"""
task :1 using numpy_dataset excel file   find the 
total month_1 units  ----> mean ,median 
total month_2 units  ----> mean ,median 
total month_3 units  ----> mean ,median 

"""
