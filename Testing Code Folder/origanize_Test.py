#file handling: Navigate, rename, move, copy, remove
#how to keep my desktop organized

import os
#shutil helps with moving files around
import shutil

from pathlib import Path


#gets current working directory 
print(os.getcwd())
print("\n")

#changing directory
os.chdir("D:\Krita\saves\png")
print(os.getcwd())
print("\n")

#get list of all files in directory
print(os.listdir())
print("\n")

#iterate (perform or utter repeatedly)
for file in os.listdir():
    if file == "data" or file == "data1":
        continue
    print(file)

print("\n")
#splitting name and extentions from a file
for file in os.listdir():
    #skips these files/folders
    if file == "data" or file == "data1":
        continue
    name, extension = os.path.splitext(file)
    print(name)
    print(extension)
    print("\n")


#creating new directorys(new folders)
#using the pathlib module
Path("data").mkdir(exist_ok=True)

#with out the pathlib module
if not os.path.exists("data1"):
    os.makedirs("data1")
'''Note when iterating it will also show any folders that may be in that directory.'''

#Moving files into a folder
for file in os.listdir():
    #skips these files/folders
    if file == "data" or file == "data1":
        continue
    #moves all file into folder. other then data1 cause we skipped it
    '''shutil.move(file, "data")'''
    #copies files into a folder.
    '''Note when copying it will make a new timestamp of the copied files'''
    shutil.copy(file, "data")
    #use copy2 to copy both the file and its timestamp
    shutil.copy2(file,"data1")

#Removing files and folder/directories
# os.remove("fikename")
# os.rmdir("foldername")
'''Note rmdir wont work is folder is not empty.'''

#deleting files in a folder and then deletes the folder
# shutil.rmtree("data")
