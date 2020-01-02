import os.path
from os import path

# Python code to create a file 
if path.exists("learnpy.txt"):
    file = open('learnpy.txt','a') 
else:
    file = open('learnpy.txt','w') 

file.write("This is the write command\n") 
file.write("It allows us to write in a particular file\n") 

file.close()