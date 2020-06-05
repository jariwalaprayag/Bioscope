import os
import ctypes  # An included library with Python install.
import distutils.core
import shutil,os,glob
#import Tkinter
#import tkMessageBox

MovieDEST = "/root/Desktop/users/movie"
PhotoDEST = "/root/Desktop/users/photo"
SongDEST = "/root/Desktop/users/song"
path = r"/root/Desktop/users/source"

MovieCounter = 0
PhotoCounter = 0
SongCounter = 0

for root, dirs, files in os.walk(path):
    for file in files:    
        if file.endswith(".mp4"):
            MovieCounter += 1
        if file.endswith(".MP4"):
            MovieCounter += 1
        if file.endswith(".mkv"):
            MovieCounter += 1
			
for root, dirs, files in os.walk(path):
    for file in files:    
        if file.endswith(".png"):
            PhotoCounter += 1
        if file.endswith(".PNG"):
            PhotoCounter += 1
			
for root, dirs, files in os.walk(path):
    for file in files:    
        if file.endswith('.mp3'):
            SongCounter += 1
	
print('Movies : ',MovieCounter)
print('Photos : ',PhotoCounter)
print('Songs : ',SongCounter)

#popup
#txt='Movies: '+str(MovieCounter)+'\nPhotos: '+str(PhotoCounter)+'\nSongs: '+str(SongCounter)+'\n Do you want to copy ???'
#result = ctypes.windll.user32.MessageBoxW(0,txt, "Media Count", 1)	 
#print(result)
#result = tkMessageBox.askyesno("Whould you like to Copy???",'Movies: '+str(MovieCounter)+'\nPhotos: '+str(PhotoCounter)+'\nSongs: '+str(SongCounter))
#print result
#copy

