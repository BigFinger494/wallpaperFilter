from PIL import Image
from pathlib import Path
from sys import argv
import time
import os
import shutil

script, first = argv
ext = (".jpeg",".jpg",".png")
counter = 0

def createDirectory():
    from pathlib import Path
    Path(f"{first}").mkdir(parents=True, exist_ok=True)
    while not os.path.exists(first[0:-1]):
        time.sleep(0.5)
    print("created newFolder")
    return (os.getcwd()+"\\"+first)

def getFiles():
    print(os.listdir(os.getcwd()))
    return os.listdir(os.getcwd())

def filterFiles():
    for file in os.listdir(os.getcwd()):
        if file.endswith(ext):
            with Image.open(file) as img:
                width, height = img.size
                img.close()
                if((height == 1080 and width == 1920) or (height == 1440 and width == 2560) or (height == 2160 and width == 3840)):
                    shutil.move(file, first + file)
                    counter += 1
    print("Done. Added", counter,"files")

def main():
    createDirectory()
    filterFiles()

if __name__ =="main":
    main()