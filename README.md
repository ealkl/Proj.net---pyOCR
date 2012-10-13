#Proj.net---pyOCR
-----------------
Currently only placeholder for some notes for the project. 

If you feel like testing it out, clone the project (launch pyOCR) and follow the instructions in the buttom of the page for instructions on how to install & compile dependencies.

Cam-interface
-----------------
* A function to interface with a (web)camera, take a picture - which we then can parse/import to a renaming & numbering function (see below). (Check)
* Need a function to store an image to the locale filesystem, and rename them numerical & incrementaly. For identification. (Check)

#OCR-function
-----------------
* Will be adding config to limit Tesseract characters (../tessdata/config/[file] & load with argument). 
* Also need to clean source image before processing (needs tweaking).
* Ability to crop image (functionality is there, however it is yet to be implemented).

Database & Archive
-----------------
* Currently the script will, after processing the picture through tesseract, copy the image to the archive directory and rename the file to the corrosponding ID stored in the MySQL.
* Also stores the time for image capture.

Print-function(?)
-----------------
* To what? Webpage, console? Suggestions :)


HOW TO
=======

##Requirements
* Python 2.6
* MySQL
* pyODBC
* OpenCV (This module is required for capturing pictures from a webcam).
* Python Image Library
* Tesseract OCR
* ImageMagick


##Installing libraries & dependencies.

###Python 2.6
* Follow instructions for Windows on python.org. Mac & Linux has it pre-installed.

###MySQL
* Install XAMPP or sorts.: http://www.apachefriends.org/en/xampp.html

###pyODBC
* Follow instructions from my previos assigntment "Technology Template".: https://github.com/ealkl/Proj.net---pyODBC

###OpenCV
* Installing on a debian-based system, can be perfomed like so: sudo apt-get update && sudo apt-get install python-opencv (Maybe also sudo apt-get install opencv).
* Installing on Mac OS using MacPorts: sudo port selfupdate && sudo port install opencv +Python2.6 (The last parameter was required, to build the python libs proberly).

###Python Image Library ("PIL")
1. Download soure: http://effbot.org/downloads/Imaging-1.1.7.tar.gz
2. In your favourite terminal cd to the root of "imaging-1.1.7.tar.gz"
3. Run the selftest "python selftest.py". 
3a. Note any missing dependencies from previous step. On my Mac I only had to install the lcms (littleCMS) through macports.
4. Build the library "python setup.py build_ext -i".
5. Installing the library is done by calling "sudo python setup install" (su is required for moving files to systemfolders, and change file permissions).
6. Import the module by calling "import Image"

###Tesseract-OCR
* Installing Tesseract on a debian based system, can be perfomed like so: sudo apt-get update && sudo apt-get install tesseract-ocr
* Installing on Mac OS, can be performed through Macports (ports): sudo port selfupdate && sudo port install tesseract
* Windows: Who knows? I think there is a precompiled binary available :)
* Remember to install Language files (I was prompted for: /opt/lib/share/tessdata/eng.traineddata). You can get the english datafiles from here: http://code.google.com/p/tesseract-ocr/downloads/detail?name=tesseract-ocr-3.01.eng.tar.gz&can=2&q=

###ImageMagick
* Use your favourite package manager to install ImageMagick like described in previous posts.