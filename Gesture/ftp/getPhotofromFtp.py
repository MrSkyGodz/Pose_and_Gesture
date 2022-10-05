import ftplib,os,time
import glob
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

datas = bytes(ip = "192.168.0.2",name = "admin",pwd = "admin")
def fetch_img_ftp():
	global datas

	ftp = ftplib.FTP("192.168.0.2","admin","admin")
	files = ftp.cwd('./nova')

	last_file = sorted(ftp.nlst(), key=lambda x: ftp.voidcmd(f"MDTM {x}"))[-1]
	print(last_file)
	
	a = ftp.retrbinary("RETR " + last_file,callback) #open(last_file, 'wb').write)

	print(datas)
	stream = BytesIO(datas)

	image = Image.open(stream)
	

	img = np.array(image)
	# print(img.shape)

	stream.close()

	datas = bytes()
	return img

	
	# print(len(a))
def callback(data):
	global datas

	datas += data

while(1):
	fetch_img_ftp()

	# cv2.imshow("asd",fetch_img_ftp())

	# cv2.waitKey(0)

	time.sleep(0.5)