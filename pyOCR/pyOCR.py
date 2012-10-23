'''
Created on Oct 8, 2012

@author: ealkl
'''
import pyodbc, shutil, subprocess, shlex, os, datetime, cv, anpr
from cv2 import *
from tesseract.pytesser import *
#this is important for capturing/displaying images
server = '192.168.227.128'
database = 'cd_inventory'
table = 'artists'
uid = 'testacc'
pwd = 'testacc'
print 'Initializing camera.\n\n'
#Should store in another "temp" directory.
camimg = VideoCapture(0)   # 0 = device
s, camimg = camimg.read()
if s:    # frame captured without any errors
#    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
#    imshow("cam-test",camimg)
#    waitKey(0)
#    destroyWindow("cam-test")
    imwrite('./tmp/temp.jpg', camimg)#("test.jpg",camimg) #save image
#ImageMagick - textcleaner script: Cleaning source picture for background noise.
#with open(os.devnull, "w") as f: #open dev/null to obj
#    subprocess.call(["./textcleaner.sh", "-g", "./tmp/temp.jpg", "./tmp/converted_image.jpg"], stderr=f) #clean image, and suppress errors. Needs some fine-tuning.
#Current time for capturing.
now = datetime.datetime.now()
capTime = now.strftime("%Y-%m-%d %H:%M")
#Restraining to a smaller area of a specific web-cam will also be preferable.
print '\n\nRunning OpenANPR by O.E.Smith'
counter = 0
image = cv.LoadImage('./tmp/temp.jpg') #possible multiple outputs. Therefore the loop.
for plate in anpr.detect_plates(image): #Need some sort of method to include all possbile outputs to 1 ID - maybe another counter and DB entry of sorts?
    cv.SaveImage('processed_temp.jpg' % counter, plate) #counter processed_temp%02d.jpg, but how to "pick up" from there?
    counter = counter+1

print '\n\nRunning picture through Tesseract OCR, by Google\n\n'
#Tesseract OCR
im = Image.open('./tmp/processed_temp.jpg') #
text = image_to_string(im)
print '\n\nPrinting output of OCR process: ' + text
#SQL connection string.
cnxn = pyodbc.connect('DRIVER={MySQL ODBC 5.1 Driver};SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
cursor = cnxn.cursor()
cursor.execute("insert into ocrplates(numberplate, timestamp) values (?, ?)", text, capTime)
cnxn.commit()
cursor.execute("SELECT @@IDENTITY") #Triggers DB id generated. This ID will be the filename of the picture.
for row in cursor.fetchall():           
    line = str(row)
    for char in line:
        if char in "()L, ": #delete chars, to clean output.
            line = line.replace(char,'')
#Archive picture with db id.
shutil.copyfile('./tmp/temp.jpg', './archive/'+line+'.jpg') #will need some re to save the file-extention and append to dst. here.
print 'Picture and data archived with filename: ' +line  +'.jpg' +' and DB id: ' +line