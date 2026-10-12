import pandas as pd
import  numpy as np 

"""
df= pd.DataFrame({
    "id" :[np.nan,2,3,4,5],
    "name" :[np.nan,"peter","paul","george","ringo"],
    "salary":[np.nan,np.nan,34000,np.nan,56000],
    "age" :[np.nan,34,np.nan,56,np.nan]
})
print("original : \n",df)
"""
# dropna  : 

"""
result = df.dropna(axis =0,how='any')   # axis 0 : row 
result = df.dropna(axis =1,how='any')  # axis 1 : col
result = df.dropna(axis =0,how='all')  # all row and col are nan then  only  remove 
print("dropna : \n",result)
"""

# sort_values , sort_index :

df= pd.DataFrame({
    "id" :[1,2,3,4,5],
    "name" :["peter","paul","george","ringo","mary"],
    "salary":[12000,24000,56000,78000,34000],
    "age" :[12,34,56,78,56]
})
print("original : \n",df)

# sort_values : 
"""
sorted_salary  = df.sort_values(by='salary')  # by default  ascending order to desc 
sorted_salary  = df.sort_values(by='salary',ascending=False)  # by default  ascending order to desc 
print("sort by salary : \n",sorted_salary)
"""

# sort_index :

# sorted_Index = df.sort_index(axis=1)  # by default  ascending order to desc
# sorted_Index = df.sort_index(axis=0,ascending=False)  # by default  ascending order to desc
sorted_salary  = df.sort_values(by='salary',ascending=False)  # by default  ascending order to desc 
print("sort by salary : \n",sorted_salary)

# print("sort by index : \n",sorted_Index)