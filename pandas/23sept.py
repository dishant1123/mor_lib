import pandas as pd
# csv  file read : 

"""df =pd.read_csv('pandas/student.csv')
print(df)

# head , tail , info ,describe ,describe_all

print(df.head(3))  # by default it shows first 5 rows
print(df.tail(3))  # by default it shows last 5 rows

print(df.info())  
print(df.describe())
print(df.describe(include='all'))
"""

# excel file read :
"""df =pd.read_excel("pandas/Region.xlsx")
print(df)
"""

# tsv file read : tab separated file

"""
df = pd.read_csv('pandas/students.tsv', sep='\t') # \t : tab
print(df)
print(df.shape)  # total  col and  rows 
print(df.columns) # print  all  column name 
"""
from sqlalchemy import create_engine

# sql file read :

"""Host     = "localhost"
Port     = 3306
Username = "root"
Password = "root"
Database = "dishant"

engine = create_engine(f"mysql+pymysql://{Username}:{Password}@{Host}:{Port}/{Database}")
df = pd.read_sql_query("select * from sale_t", engine)
print(df)
"""

# create  dataframe : 
"""
2 ways  : 

1 .dict
2. list
"""
# using dict dataframe :
"""df = pd.DataFrame({
    "id" : [1,2,3,4,5],
    "name" : ["john","peter","paul","george","ringo"],
    "age" : [20,30,35,40,45],
    "salary" : [1000,3000,4000,5000,6000]
})

print(df)
print(df.columns)
print(df.shape)
print(df.keys())
print(df.values) 
"""

# using list dataframe :

df =pd.DataFrame([
    [1,"john",20,1000],
    [2,"peter",30,3000],
    [3,"paul",35,4000],
    [4,"george",40,5000],
    [5,"ringo",45,6000],
    [6,"mary",25,2000]
],columns=["id","name","age","salary"])

print(df)
print(df.shape) 

