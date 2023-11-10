import os
import shutil
import schedule
import time

def move_files():
    path = "/Users/wilson/Downloads/"

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

    # desktop
    path = "/Users/wilson/Desktop/"

    # screenshots
    if not os.path.exists(path + 'screenshots/'):
        os.makedirs(path + 'screenshots/')

    for file2 in os.listdir("/Users/wilson/Desktop"):
        if 'Screenshot' in file2 and not os.path.exists(path + 'screenshots/' + file2):
            shutil.move(path + file2, path + 'screenshots/' + file2)

# schedule the job to run every minute
schedule.every(1).minutes.do(move_files)

# run the scheduler in a loop
while True:
    schedule.run_pending()
    time.sleep(1)  # sleep for 1 second to avoid high CPU usage