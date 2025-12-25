import numpy as np

data=[2,3,5,8]
print("Range : ",(max(data)-min(data)))

print(np.percentile(data,[0,25,50,75,100]))

print("IQR : ",np.percentile(data,[25])-np.percentile(data,[75]))


#Outlier >> outside the boxplot are the outlier it can be directly seen in the the graph as outlier
# import seaborn as sns
# sns.boxplot(data) 

#Variance
print("Variance : ",np.var(data))
print("Standard deviation  :",np.std(data))

import statistics
print("Sample Variance : ",statistics.variance(data))
print("Population Variance : ",statistics.pvariance(data))