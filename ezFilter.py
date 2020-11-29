from PIL import Image
from sys import argv
import time
import os
import shutil

script, first = argv
ext = (".jpeg",".jpg",".png")
counter = 0

from pathlib import Path
Path(f"{first}").mkdir(parents=True, exist_ok=True)
while not os.path.exists(first[0:-1]):
    time.sleep(0.5)

for file in os.listdir(os.getcwd()):
    if file.endswith(ext):
        with Image.open(file) as img:
            width, height = img.size
            img.close()
            if((height == 1080 and width == 1920) or (height == 1440 and width == 2560) or (height == 2160 and width == 3840)):
                shutil.move(file, first + file)
                counter += 1
print("Done. Added", counter,"files")
