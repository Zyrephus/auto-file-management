import os
import shutil

path = "/Users/wilson/Downloads/"
desktop = "/Users/wilson/Desktop/"

file_name = os.listdir(path)

# folders
folder_names = ['pdf files/','png files/', 'jpg and jpeg files/', 'gif files/']

for loop in range(0, 4):
    # if the folder doesn't exist in Downloads aready
    if not os.path.exists(path + folder_names[loop]):
        # makes the folders in folder_names
        os.makedirs(path + folder_names[loop])


# moving file into files
for file in file_name:
    # if file is pdf and isn't already in pdf files
    if '.pdf' in file and not os.path.exists(path + 'pdf files/' + file):
        shutil.move(path + file, path + 'pdf files/' + file)
    # pngs
    elif '.png' in file and not os.path.exists(path + 'png files/' + file):
        shutil.move(path + file, path + 'png files/' + file)
    # jpgs and jpegs
    elif ('.jpg' in file or '.jpeg' in file) and not os.path.exists(path + 'jpg andjpeg files/' + file):
        shutil.move(path + file, path + 'jpg and jpeg files/' + file)
    # GIFs
    elif '.gif' in file and not os.path.exists(path +'gif files/' + file):
        shutil.move(path + file, path + 'gif files/' + file)