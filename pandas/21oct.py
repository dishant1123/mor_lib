# merge  : 
"""
1. inner join   :
2. left join    : 
3. right join   : 
4. outer join   :  

"""

import pandas as pd

# First DataFrame
"""df_customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

# Second DataFrame
df_orders = pd.DataFrame({
    'customer_id': [1, 2, 2, 4],
    'order_id': [101, 102, 103, 104],
    'amount': [250, 100, 150, 300]
})

print(df_customers)
print(df_orders)
"""
# inner join : 
"""inner_join =pd.merge(
    df_customers,
    df_orders,
    on='customer_id',
    how = 'inner'
)
print("inner join \n", inner_join)
"""
# left_join : left table  saare aayge right table matching value ayegi 

"""
left_join = pd.merge(
    df_customers,  
    df_orders,  
    how = 'left',
    on='customer_id'
)
print("left join \n", left_join)
"""
"""
left join 
    customer_id     name  order_id  amount
0            1    Alice     101.0   250.0
1            2      Bob     102.0   100.0
2            2      Bob     103.0   150.0
3            3  Charlie       NaN     NaN
4            4    David     104.0   300.0
"""
"""right_join = pd.merge(
    df_customers,  
    df_orders,  
    how = 'right',
    on='customer_id'
)
print("right join \n", right_join)
"""
"""
right join 
    customer_id   name  order_id  amount
0            1  Alice       101     250
1            2    Bob       102     100
2            2    Bob       103     150
3            4  David       104     300
"""

# outer join :
"""outer_join = pd.merge(
    df_customers,
    df_orders,
    how = 'outer',
    on='customer_id'
)
print("outer join \n", outer_join)
"""

# concat : 
"""
two_tables_concat = pd.concat([df_customers, df_orders], axis=1)
two_tables_concat = pd.concat([df_customers, df_orders], axis=0)

print("concat \n", two_tables_concat)
"""
# tasks  
"""
1. movies and directors ------> merge -----> movies ----> director_id  directos ----> id 
2. unamed col  drop  with  both movies and directors
3. top 5 movie name earns  highest revenue
"""

movies = pd.read_csv('pandas/movies.csv')
print(movies.head())
