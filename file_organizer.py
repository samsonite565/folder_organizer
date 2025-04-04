"""
Title: Folder Organizer
Author: Samson Thomas
Date: December 30, 2023
Version: 1.0
Python-version: 3.12.8
 
A simple program to organize files based on the extentions provied. Feel free to modify
the code. To modify the extentions just add extentions to the dictionary called "SUBDIR". 
If you feel the code could be improved please fork the code and make the necceary changes. 
I am an new coder and just learning the basics. Thank you!

Copyright (c) 2023


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE

(The head description is taken from @Jan B. )
Ref. Link: https://github.com/b01jan/Downloads-organizer/blob/master/organize.py
"""

import pyfiglet
import os
from pathlib import Path

SUBDIR = {
    "Docs": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".epub", ".csv"],
    "Audio_Video": [".mp4", ".mp3", ".gif", ".svg", ".tiff"],
    "Images": [".jpg", ".png", ".jpeg", ".psd"],
    "Codes": [".py", ".json"],
    "Other": [".iso"],
}


def main():
    print(pyfiglet.figlet_format("Directory Organizer", font="slant"))
    path = input("Copy and past the path: \n").strip('"')
    raw_path = repr(path)[1:-1]
    organize(raw_path, SUBDIR)


def organize(path: str, file_types: dict):
    for item in os.scandir(path):
        file_path = Path(item)
        file_ext = file_path.suffix.lower()

        for category, extentions in file_types.items():
            if file_extention in extentions:
                # Creates the folder
                new_folder = os.path.join(path, category)
                os.makedirs(new_folder, exist_ok=True)
                # Puts the files into the created folder based
                new_path = os.path.join(new_folder, file_path.name)
                os.rename(file_path, new_path)
            else:
                if not os.listdir(path):
                    print("Folder is empty")


if __name__ == "__main__":
    main()
