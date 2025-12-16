# file=open('file.text',"w")


# #File attribute

# file.write("How are you bro")
# file.close()

# file=open("file.txt","w")
# file.write("Previous content deleted")
# file.write("Previous content deleted Line 2")
# file.write("Previous content deleted Line 3")
# file.close()


# file= open("file.text","a")
# file.write("This is my fifth Line ")
# file.close()


file= open("file.text","r")
for i  in file:
    print(i)


# file.tell() #current postion of the cursor
file.seek(0)
file.read()
file.readline()
file.readlines()