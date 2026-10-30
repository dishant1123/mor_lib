import  pandas as pd 
import matplotlib.pyplot as plt
import  numpy as np  

"""
pip install matplotlib.pyplot : 

---> basic graph  and  plot  
---> graph : 
    1. plt.plot() : line graph
    2. plt.bar() : bar graph
    3. plt.scatter() : scatter graph
    4. plt.hist() : histogram graph
    5. plt.pie() : pie chart
    6.plt.box() : box plot -----> outlier detection

attributes / properties of graph :
    1.plt.xlabel() ,plt.ylabel() 
    2. plt.title() 
    3. plt.legend() -----> corner of graph ----> mark 
    4. plt.grid() -----> grid lines 
    5. plt.show() -----> display graph
    
"""

# line  plot  : 

"""days = [1,2,3,4,5,6,7,8,9]
sales =[100,200,150,170,190,250,160,300,400]

plt.plot(
    days,
    sales,
    color = 'green',  # 
    marker = 'o',  # intercept x and y  ----> o 
    linestyle = '--',  # ----
    linewidth = 2   # line thickness
   
)
plt.xlabel('Days')  # x axis label
plt.ylabel('Sales')  # y axis label
plt.title('Sales vs Days')  # title of graph
plt.grid(True)  # grid lines 
plt.legend(['Sales'],loc='upper left')  # legend of graph
plt.show()  # display graph

"""

# line  graph using csv file  : 

"""df = pd.read_csv("matplotlib/days_sales.csv")

plt.plot(
    df['Day'],
    df['Sales'],
    color = 'blue',  #
    marker = 'o',  # intercept x and y  ----> o
    linestyle = '--',  # ----
    linewidth = 2   # line thickness
)
plt.xlabel('Days')  # x axis label
plt.ylabel('Sales')  # y axis label
plt.title('Sales vs Days')  # title of graph
plt.grid(True)  # grid lines
plt.legend(['Sales'],loc='upper left')  # legend of graph
plt.show()  # display graph
"""

# create bar graph  :

"""import sqlalchemy as sa

Username = "root"
Password = "root"
host = "localhost"
port = 3306
create_engine = sa.create_engine(
    "mysql+pymysql://root:root@localhost:3306/dishant")

df =pd.read_sql("select * from sale_t",create_engine)
print(df)

data =pd.DataFrame(df)

plt.plot(
    data['sale_id'],
    data['amount'],
    color = 'blue',  #
    marker = 'o',  # intercept x and y  ----> o
    linestyle = '--',  # ----
    linewidth = 2   # line thickness
)

plt.xlabel('Sale ID')  # x axis label
plt.ylabel('Amount')  # y axis label
plt.title('Amount vs Sale ID')  # title of graph
plt.grid(True)  # grid lines
plt.legend(['Amount'],loc='upper left')  # legend of graph
plt.show()  # display graph

"""

# plt.bar () :
df = pd.read_csv("matplotlib/student_marks (1).csv")
plt.figure(figsize=(8, 5))  # box size of graph
plt.bar(df['name'], 
        df['marks'],
        color='orange', 
        width=0.5,
        edgecolor='black')  # bar graph

plt.xlabel('Name')
plt.ylabel('Marks')
plt.title('Marks vs Name')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.legend(['Marks'])
plt.show()