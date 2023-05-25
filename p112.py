import os
import shutil

from_dir =  "C:/Users/Pranjal Kadam/Downloads"
to_dir = "C:/Users/Pranjal Kadam/Desktop"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    if extension  == "":
        continue
    if extension in ['.pdf','.txt','.doc','.docx']:
        path1 = from_dir + '/' + file_name
        print(path1)
        path2 = to_dir + '/' + "screenshots"
        print(path2)
        path3 = to_dir + '/' + "screenshots" + '/' + file_name
        print(path3)

        if os.path.exists(path2):
            print("moving the "+ file_name + "...")
            shutil.move(path1,path3)

        else:
            os.mkdir(path2)
            print("creating the folder in the destination path")
            print("moving the "+ file_name + "...")
            shutil.move(path1,path3)





    