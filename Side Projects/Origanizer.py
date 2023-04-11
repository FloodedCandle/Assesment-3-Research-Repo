import os
import shutil

print("[1] organize a folder.")
print("[2] unpack folder.(W.I.P)")
print("[0] Exit.")
option = int(input("Selecet option: "))

while option != 0:
    
    if option == 1:
        #user inputs file directory/path
        path = input("Enter path to organize: ")
        #give list of all file in givin directory.
        files = os.listdir(path)

        #create list of all files
        for file in files:
            filename, extentsion = os.path.splitext(file)
            extentsion = extentsion[1:]

            #if folder for file with the same extentsion exists move file to that folder.
            if os.path.exists(path + '/' + extentsion):
                shutil.move(path + '/' + file, path + '/' + extentsion + '/' + file)
            #if file does not have a folder make new with using extenstion to name folder.
            else:
                os.makedirs(path + '/' + extentsion)
                shutil.move(path + '/' + file, path + '/' + extentsion + '/' + file)

        
    #W.I.P
    elif option == 2:
        #users enters directory/path they want to unpack(remove files inside folder)
        source_dir = input("Enter path to unpack: ")

        #user enters final directory/path where the unpacked files will end up.
        destination_dir = input("Enter final path where unpack will go to: ")

        #get a list of the files in the folder
        files = os.listdir(source_dir)

        #iterating moving process
        for file in files:
            shutil.move(file, destination_dir)
            

        
    
    else:
        print("Invalid option.")
        
    print("[1] organize a folder.")
    print("[2] unpack folder.")
    print("[0] Exit.")
    option = int(input("Enter your option: "))
    
    
print("shut down!")