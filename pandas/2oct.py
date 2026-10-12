# dropna  : 
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'id' : [1,2,3,4,5,6,7,8,9,10],
    'name' : ["john","peter","paul",np.nan,"ringo","mary","sujal","tisha","vansh","nikhil"],
    'age' : [20,np.nan,35,40,45,25,np.nan,10,9,8],
    'salary' : [1000,3000,4000,5000,6000,2000,3000,200,900,800]
    
})
print(df)

# dropna , sort_values , sort_index : 
