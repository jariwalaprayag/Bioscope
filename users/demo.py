import os
import ctypes  # An included library with Python install.
import distutils.core
import shutil,os,glob
#import Tkinter
#import tkMessageBox

path = r"/root/Desktop/users/source"
MovieDEST = "/root/Desktop/users/photo"
for root, dirs, files in os.walk(path):
	for file in files:    
		if file.endswith(".png"):
			print(files)
			shutil.copy(file,MovieDEST)

