# Works very well with the structured way
import pandas as pd

# pd.read_csv('services', header=None)

# pd.read_csv("services",skiprows=2)
# pd.read_csv("services",usecols=['program_id','application_process'])

#Data frame structure of data

#Data structures >> series and dataframe
#series >> 1 dimensional in nature, multiple series constitutes to form  dataframe

# df=["application_process"] #>> it is series
# df.application_process()

l=[1,2,3,4]
s=pd.Series(l)
# print(type(s))

# print(s[2:4])

d=pd.Series([100,200,300] , index=["Ajay","Vijay","Sanjay"])
# print(d)
# print(d.index)
# print(d["Ajay":"Sanjay"])

d.reset_index(drop=True)
f=pd.DataFrame(d)
# print(f)
# print(f.shape)
# print(f.head(2))
# print(f.tail(1))
# print(f.sample(2)) #>> 2 random row
# print(f.info) # datatype of entry
# print(f.) # datatype of entry

#series to datadframe
x=pd.DataFrame(d)
# x["col_name"]
# x[["col_name","col_2","col_3"]] #subset dataframe
# x.col_name
# print(x)

x.columns=["Salary"]
print(x)

x.reset_index()
print(
x.reset_index())
print(x.reset_index(drop=True)) #Purana index cokumn ban jayegs


# ex=pd.read_excel("name.xlsx")
# ex.columns
# ex.dtypes
# ex.info()

pd.read_csv("linkofsrc")

#Read table from HTML Site all the table data
import lxml 
pd.read_html("url")


#Creating the data to csv file
# x.to_csv("name",index=False)

url= ""
pd.read_json(url)


import requests
data=requests.get(url)

print(data)