import matplotlib.pyplot as plt 
import  pandas as pd 

# line  plot  : 
"""days = [1,2,3,4,5,6,7,8,9]
sales =[200,150,130,500,290,450,600,700,900]

plt.plot(
    days,  # -----> x 
    sales,  # -----> y 
    color="red",
    linestyle=":", 
    linewidth=2,
    marker='*'
)
plt.xlabel("days")
plt.ylabel("sales")
plt.title("Sales vs Days  line graph")
plt.legend("sales",loc="upper right")
plt.grid(True) 
plt.show()
"""

# using pandas create  line  graph : 

"""
df= pd.read_csv("matplotlib/student_marks (1).csv") 

plt.figure(figsize=(10,8))
plt.plot(
    df['id'],
    df['marks'],
    color="red",
    linestyle=":", 
    linewidth=2,
    marker='*'
    )
plt.xlabel("id")
plt.ylabel("marks")
plt.title("id vs marks  line graph")
plt.legend("marks",loc="upper left")
plt.grid(True) 
plt.show()
    
"""

# plt.bar():
df= pd.read_csv("matplotlib/student_marks (1).csv") 

plt.figure(figsize=(10,8))

plt.bar(
    df['name'],
    df['marks'],
    color="green"

)
plt.xlabel("name")
plt.ylabel("marks")
plt.title("name vs marks bar plot")
plt.xticks(rotation=45)
plt.legend("marks",loc="upper left")
plt.show()