import pandas as pd
import numpy as np
"""
df = pd.DataFrame({
    'id' : [1,2,3,4,5,6,7,8,9,10],
    'name' : ["john","peter","paul","george","ringo","mary","sujal","tisha","vansh","nikhil"],
    'age' : [20,30,35,40,45,25,13,10,9,8],
    'salary' : [1000,3000,4000,5000,6000,2000,3000,200,900,800]
    
})

print(df)
"""
# query () : print  only  those employees whose salary is more than  3000  print  only name, salary. 

# loc , iloc : 

"""result = df.query("salary > 3000")[['name','salary']]
print(result)
"""

# handling  missing  value :

df = pd.DataFrame({
    'id' : [1,2,3,4,5,6,7,8,9,10],
    'name' : ["john","peter","paul","george","ringo","mary","sujal","tisha","vansh","nikhil"],
    'age' : [20,30,35,40,45,25,13,10,9,8],
    'salary' : [1000,3000,4000,5000,6000,2000,3000,200,900,800]
    
})
# print(df)

# null value count col wise :  isna() .sum(): 
# print(df.isna().sum())

# missing  value handle  with : fillna()
"""
df['name'] = df['name'].fillna("unknown")
# salary fill with mean of  salary  : 
df['salary'] = df['salary'].fillna(df['salary'].mean())

#age  fill with median of  age :
df['age'] = df['age'].fillna(df['age'].median())

# id  fill with mean of  id :
df['id'] = df['id'].fillna(df['id'].mean())
print(df)
"""

# drop  : delete the  col 

# df.drop('name',axis =1,inplace = True)

# df=df.drop('name',axis =1)
# df=df.drop(0,axis =0)
df=df.drop(['id','age'],axis =1)
print(df)

# dropna : next session 
