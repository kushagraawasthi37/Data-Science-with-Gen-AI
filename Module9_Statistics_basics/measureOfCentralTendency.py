import numpy as np
age=[1,2,1,3,24,25,64,98]

#Mean measure manual way
sum=0
for i in age:
    sum+=i

#Divide the sum by number of element

print("Mean : ",sum/len(age))

#calculate the median using the manual way

sorted(age)
size=len(age)
if(size%2==0):
    print("Median : ",age[int(size/2)]+age[int(size/2+1)]/2)
else:
    print("Median : ",age[int(size/2)])


#Central Tendency->using the numpy library
print("Mean : ",np.mean(age))
print("Median : "  ,np.median(age))

import statistics
print("Mode : ",statistics.mode(age))

#Outlier affects the mean but doesn't affect the median