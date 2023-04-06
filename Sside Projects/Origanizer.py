import os
import shutil

print("[1] organize a folder.")
print("[2] unpack folder.")
print("[0] Exit.")
option = int(input("Selecet option: "))

while option != 0:
    if option == 1:
        path = input("Enter path to organize: ")
        files = os.listdir(path)

        for file in files:
            filename, extentsion = os.path.splitext(file)
            extentsion = extentsion[1:]

        if os.path.exists(path + '/' + extentsion):
            shutil.move(path + '/' + file, path + '/' + extentsion + '/' + file)
        else:
            os.makedirs(path + '/' + extentsion)
            shutil.move(path + '/' + file, path + '/' + extentsion + '/' + file)

        

    elif option == 2:
        source_dir = input("Enter path to unpack: ")
        destination_dir = "C:\\Users\\20220020\\Desktop\\folders" #input("Enter final path where unpack will go to: ")
        files = os.listdir(source_dir)

        for file in files:
            file_path = os.path.join(source_dir,file)
            if os.path.isfile(file_path):
                shutil.move(file_path, destination_dir)

    
    else:
        print("Invalid option.")
        
    print("[1] organize a folder.")
    print("[2] unpack folder.")
    print("[0] Exit.")
    option = int(input("Enter your option: "))
    
    
