import os
import shutil
import glob

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

trash_path = os.path.join(os.path.expanduser('~'), '.Trash')

screenshot_pattern = "Screenshot*"

# Find all screenshots on the Desktop
screenshots = glob.glob(os.path.join(desktop_path, screenshot_pattern))

# Move each screenshot to the Trash
for screenshot in screenshots:
    try:
        # Construct the destination path in the Trash
        dest_path = os.path.join(trash_path, os.path.basename(screenshot))
        # Move the screenshot to the Trash
        shutil.move(screenshot, dest_path)
        print(f"Moved to trash: {screenshot}")
    except Exception as e:
        print(f"Error moving file {screenshot}: {e}")

print("All matching screenshots have been moved to the Trash.")