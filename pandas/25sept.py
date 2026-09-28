import pandas as pd

# filtering dataframe
"""
1. loc 
2. iloc 
3. query
"""

df = pd.DataFrame({
    'id' : [1,2,3,4,5,6,7,8,9,10],
    'name' : ["john","peter","paul","george","ringo","mary","sujal","tisha","vansh","nikhil"],
    'age' : [20,30,35,40,45,25,13,10,9,8],
    'salary' : [1000,3000,4000,5000,6000,2000,3000,200,900,800]
    
})

print(df)

# loc : label  based 

"""result = df.loc[2:5]  # both  point  included  row  
result  = df.loc[2:5,"name":"salary"]  # row  ----> number  ,col ----> col_name 
result  = df.loc[2:5,['name','salary']]  # row  ----> number  ,col ----> name ,salary
print(result)
"""

# iloc : index  based
"""
result  = df.iloc[2:5]  # last number  excluded 
result  = df.iloc[2:5,1:3]  # row  : 2:5 , col 1:3 
result  = df.iloc[1:5:3, : : 1]
print(result)

"""

# different  between  loc  and  iloc

# task  :1 
"""
create a new col as increment_salary  : give  all employees salary  +1000 

  id    name  age  salary   inc_salary
0   1    john   20    1000    2000
1   2   peter   30    3000    4000
2   3    paul   35    4000
3   4  george   40    5000
4   5   ringo   45    6000
5   6    mary   25    2000
6   7   sujal   13    3000
7   8   tisha   10     200
8   9   vansh    9     900
9  10  nikhil    8     800


"""
