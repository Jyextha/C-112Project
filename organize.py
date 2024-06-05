import os
import shutil
from_dir="C:/Users/LENOVO/Downloads"
to_dir="E:/copydata"
list_of_files=os.listdir(from_dir)
# Move all the images from the download folder to the other folder
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['gif','jpg','jpeg','jfif']:
        path1=from_dir + '/' + file_name
        path2=to_dir + '/' + "Image_Files"
        path3=to_dir + '/' + "Image_Files" + '/' + file_name

        if os.path.exists(path2):
            print("moving"+file_name+"---")
            shutil.move(path1,path3)
        else: 
            os.makedirs(path2)
            print("moving"+file_name+"---")
            shutil.move(path1,path3)
            
