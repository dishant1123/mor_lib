# pandas : pip install pandas
"""
use : 

1.data  cleaning 
2.EDA : exploratory data analysis 
3.data  visualization
4.data  transformation

ex : SQL VS  Pandas

1.SQL ----> data store  pandas ----> data  analysis

"""
import pandas as pd
import numpy as np

# series :
"""
s1= pd.Series([12,34,56,78,90])
print(s1)
print(type(s1))

s2= pd.Series([12,"tisha",56,78,90])
print(s2)
print(type(s2))


s3=pd.Series([12,34,56,78,90],index=["ram","shyam","laxman","mayank","tisha"])
print(s3)
print(type(s3))

s4 =pd.Series({
    "ram" :90 ,
    "shyam" :12 ,
    "laxman" :34 ,
    "mayank" :56 ,
    "tisha" :78
})
print(s4)
s4['ram']=56
print(s4)


s5=pd.Series([12,34,np.nan,78,90],index=["ram","shyam","laxman","mayank","tisha"],name="student")
print(s5)
# s5['laxman']=99
s5[2]=99
print(s5)
"""