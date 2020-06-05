import xbmcaddon
import xbmcgui
import pyudev
import os
import ctypes  # An included library with Python install.
import distutils.core
import shutil,os,glob

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        #print('{} connected'.format(device))
	#print("pqr")
	addon       = xbmcaddon.Addon()
	addonname   = "Media Found"
 
	MovieDEST = "/media/TOSHIBA/movie/"
	PhotoDEST = "/media/TOSHIBA/Photos"
	SongDEST = "/media/TOSHIBA/Songs"
	path = r"/media/MSTHENIL/"
	sourcepath = "/media/MSTHENIL/"
	
	MovieCounter = 0
	PhotoCounter = 0
	SongCounter = 0
	TvshowCounter = 0
		
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
	
	line1 = "Movies : "+str(MovieCounter)+"    TV Shows : "+str(TvshowCounter) 
	line2 = "Songs : "+str(SongCounter)+"    Photos : "+str(PhotoCounter)
	line3 = "Would you like to copy these files in internal drive ?"
		
	abc = xbmcgui.Dialog().yesno(addonname, line1, line2, line3)
	
	source = os.listdir("/media/MSTHENIL/")
	if abc:
		for files in source:
			if files.endswith(".png"):
				new_source = sourcepath + files
				shutil.copy2(new_source,PhotoDEST)
	
		for files in source:
			if files.endswith(".jpg"):
				new_source = sourcepath + files
				shutil.copy2(new_source,PhotoDEST)
			
		for files in source:
			if files.endswith(".mp4"):
				new_source = sourcepath + files
				shutil.copy2(new_source,MovieDEST)
			
		for files in source:
			if files.endswith(".mkv"):
				new_source = sourcepath + files
				shutil.copy2(new_source,MovieDEST)
			
		for files in source:
			if files.endswith(".mp3"):
				new_source = sourcepath + files
				shutil.copy2(new_source,SongDEST)
			
		xbmcgui.Dialog().ok("", "Copied Successfully!", "", "")