import pandas as pd 
import numpy as np 
import  matplotlib.pyplot as plt 
import seaborn as sns 
# pivort  table in  pandas : 

"""sales_data = pd.DataFrame({
    "Date": [
        "2026-01-01", "2026-01-01", "2026-01-02",
        "2026-01-02", "2026-01-03", "2026-01-03",
        "2026-01-04", "2026-01-04"
    ],
    "Region": [
        "North", "South", "North", "South",
        "East", "West", "East", "West"
    ],
    "Product": [
        "Laptop", "Laptop", "Mouse", "Mouse",
        "Keyboard", "Keyboard", "Laptop", "Mouse"
    ],
    "Sales": [
        50000, 45000, 5000, 6000,
        8000, 7000, 55000, 6500
    ]
})

print(sales_data)

result = pd.pivot_table(sales_data,
                        columns=["Product","Region"],
                        values="Sales",
                        aggfunc="sum"
                        )

print("\n",result)
"""
# EDA : exploratry data analysis 

"""
1.calculate the sales   = price *qty 
2.univarite analysis : age distribution  ,product frequency  : using value_count (),city frequency ,avg rating 
3.histogram  :age , boxplot :price
4. bivariate analysis :analysis of  two variable 
	a. sales vs age  :scatter 
	b. qty vs sales :scatter 
	c. product wise avg sales 
	d. Gender-wise Average Sales
	e. City-wise Sales
	f. Product vs Quantity
5. stats :sales mean , median ,mode , std ,var 
6. correlation  : corr(number)
	Close to 1 → Strong positive relationship
	Close to -1 → Strong negative relationship
	Close to 0 → No linear relationship

"""

"""sales_data = pd.DataFrame({
    "Customer_ID":[101,102,103,104,105,106,107,108,109,110],
    "Age":[22,25,28,40,30,45,26,38,50,33],
    "Gender":["Male","Female","Female","Male","Female","Male","Male","Female","Male","Female"],
    "City":["Ahmedabad","Surat","Rajkot","Ahmedabad","Vadodara",
            "Surat","Rajkot","Ahmedabad","Vadodara","Surat"],
    "Product":["Laptop","Mobile","Laptop","Tablet","Mobile",
               "Laptop","Tablet","Mobile","Laptop","Tablet"],
    "Quantity":[1,2,1,3,2,1,4,2,1,3],
    "Price":[65000,25000,70000,30000,22000,68000,28000,24000,72000,32000],
    "Rating":[4.8,4.2,4.6,4.0,3.8,4.9,4.1,4.3,4.7,4.2]
})
print(sales_data)
"""
"""sales_data["Total_sales"] = sales_data["Price"] *sales_data["Quantity"] 
print(sales_data)
"""

# corr : 

"""graph = sales_data.corr(numeric_only=True)

sns.heatmap(data=graph,annot=True,cmap="coolwarm")
plt.show()
"""

import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("pandas/flipkart_orders.csv")

report = ProfileReport(
    df,
    title="EDA report"
)

report.to_file("report.html")

# sweetviz  lib -----> using generate the EDA report     