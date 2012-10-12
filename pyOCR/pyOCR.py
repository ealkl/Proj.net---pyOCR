'''
Created on Oct 8, 2012

@author: ealkl
'''
import pyodbc, shutil
from cv2 import *
#this is important for capturing/displaying images

server = '192.168.227.128'
database = 'cd_inventory'
table = 'artists'
uid = 'testacc'
pwd = 'testacc'
#picture = 'test.png' #test.jpg

#Should store in another "temp" directory.

camimg = VideoCapture(0)   # 0 = device
s, camimg = camimg.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",camimg)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite('test.jpg', camimg)#("test.jpg",camimg) #save image

#Tesseract OCR
from tesseract.pytesser import *
im = Image.open('test.jpg')
text = image_to_string(im)
print text
#SQL connection string.
cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.1 Driver};SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
cursor = cnxn.cursor()
cursor.execute("insert into ocrplates(numberplate) values (?)", text) #format reason: more Columns?
cnxn.commit()
cursor.execute("SELECT @@IDENTITY") #Triggers DB id generated.
for row in cursor.fetchall():           #This ID will be the filename of the picture.
    line = str(row)
    for char in line:
        if char in "()L, ": #delete chars, to clean output.
            line = line.replace(char,'')
#Archive picture with db id.
shutil.copyfile('test.jpg', './archive/'+line+'.jpg') #will need some re to save the file-extention and append to dst. here.
print line