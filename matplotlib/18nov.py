import matplotlib.pyplot as plt 
import  pandas as pd 

#pie chart  : 

"""data =pd.DataFrame({
    "company":['Apple',"Google pixel","oppo","vivo","Real ME","Samsung"],
    "market_share" :[80,70,40,50,20,15]
    
})
"""
"""
plt.pie(
    data['market_share'],
    labels =data['company'],
    autopct='%1.1f%%',
    shadow=True
    
)
plt.title("Market share of mobile phones")
plt.show()
"""
# task  : sample super store  -----> pie  chart   , donut  
# donut  chart : 
"""plt.pie(
    data['market_share'],
    labels =data['company'],
    autopct='%1.1f%%',
    wedgeprops={'edgecolor':'black','linewidth':2,'width':0.2}
    
)
plt.title("Market share of mobile phones")
plt.show()
"""
# box  plot  : to detect outliers 

data = pd.DataFrame({
    "company":['Apple',"Google pixel","oppo","vivo","Real ME","Samsung"],
    "sales" :[800,700,405,500,200,2500]

})
plt.boxplot(data['sales'])
plt.show()

"""
task  : 
outlier  detect : 
1. IQR :  using IQR method  print  the  outlier  
2. z-score :   using  z-score  print the  outlier  
    from scipy import stats   ------> zscore  
    
    zscore >2  -----> outlier 

"""




