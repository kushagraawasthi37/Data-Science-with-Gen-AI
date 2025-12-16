text_content= """
example 1
example 2
example 3
"""
with open("example.txt","w" ) as file:
    file.write(text_content)

with open ("example.txt","r") as file:
    data= file.read()

print(data)

import csv

data=[['Name','Course',"Fee"],['Ajay',"Vijay","Kushagra"],["Pw","SCS","AC"]]

with open("example_csv.csv","w" ) as f:
    w=csv.writer(f)
    for i in data:
        w.writerow(i)

with open("example_csv.csv","r") as f:
    r= csv.reader(f)
    for i in r:
        print(i)


# Do same for 
# json file
# Binary fil
# BufferReade