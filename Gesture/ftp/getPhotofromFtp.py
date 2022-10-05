import ftplib,os,time
import glob
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import re


def fetch_img_ftp(ip = "192.168.137.1",name = "beexie",pwd = ""):
	global datas
	datas = bytes()

	ftp = ftplib.FTP(ip,name,pwd)
	ftp.cwd('./nova')

	#last_file = sorted(ftp.nlst(), key=lambda x: ftp.voidcmd(f"MDTM {x}"))[-1]
	
	#print(last_file)

	files = ftp.nlst()
	# f = lambda s: re.findall(r'\d+',s)[2]

	# print(f(files[0]))
	last_file = sorted(files,key = lambda s: int(re.findall(r'\d+',s)[2]))[-1]
	print(last_file)

	
	a = ftp.retrbinary("RETR " + last_file,callback) #open(last_file, 'wb').write)

	#print(datas)
	stream = BytesIO(datas)

	image = Image.open(stream)
	

	img = np.array(image)
	# print(img.shape)

	stream.close()

	datas = bytes()
	return img




def callback(data):
	global datas

	datas += data

# while(1):
# 	# fetch_img_ftp()

# 	cv2.imshow("asd",fetch_img_ftp())

# 	cv2.waitKey(1)

# 	time.sleep(0.5)