import pandas as pd 
import  numpy as np 
import  matplotlib.pyplot as plt

# bar  chart :  category  vs sales 
"""
category    sales 

furniture   780000 
ofc supp    650000 
tech        450000
"""

"""
df =pd.read_csv("matplotlib/sample_superstore.csv")

category_wise = df.groupby("Category")["Sales"].sum() 
print(category_wise)

# graph : 
bars =plt.bar(
    category_wise.index, # x
    category_wise.values, # y 
    color = ["red","blue","green"] 
)
plt.title("category vs sales")
plt.bar_label(bars,padding=2,fmt="%.2f",fontsize=8)
plt.xlabel("category")
plt.ylabel("sales")
plt.show()
"""
#barh :
"""
df =pd.read_csv("matplotlib/sample_superstore.csv")

category_wise = df.groupby("Category")["Sales"].sum() 
print(category_wise)

# graph : 
bars =plt.barh(
    category_wise.index, # x
    category_wise.values, # y 
    color = ["#F4C2C2","blue","green"] 
)
plt.title("category vs sales")
plt.bar_label(bars,padding=2,fmt="%.2f",fontsize=8)
plt.xlabel("category")
plt.ylabel("sales")
plt.show()
"""

# trend line  :  monthly trend line  

df =pd.read_csv("matplotlib/sample_superstore.csv")

df['Order Date']=pd.to_datetime(df['Order Date'])
df['Month']=df['Order Date'].dt.to_period('M')

monthly_wise =df.groupby("Month")['Sales'].sum() 

print(monthly_wise)

X=np.arange(len(monthly_wise))  # [0 1 ....47]
slope,intercept =np.polyfit(X,monthly_wise.values,1)
trend = slope*X +intercept

# regression  line  :  y = mx +c    -----> slope   ,  intercept  

plt.figure(figsize=(10,6))
plt.plot(
    monthly_wise.index.astype(str),
    monthly_wise.values,
    color="red",
    label="monthly sales",
    marker="o",
    linewidth=2
)

plt.plot(
    monthly_wise.index.astype(str),
    trend,
    color="blue",
    label="trend line",
    marker="o",
    linewidth=2,
    linestyle="--"
)
plt.title("monthly sales trend line")
plt.xlabel("month")
plt.xticks(rotation=45)
plt.ylabel("sales")
plt.legend()
plt.grid()
plt.show()


"""
exp_yrs   salary  
0         25000 
1         30000 
2         34000 
3         40000
4         50000
5         60000  

"""
