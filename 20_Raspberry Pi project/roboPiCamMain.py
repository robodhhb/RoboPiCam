#!/usr/bin/python3
############################################################
# File: roboPiCamMain.py
# This is the main application file for the RoboPiCam.
# It implements object detection with the Coral USB
# Accelerator (Edge TPU Coprocessor) using a model
# trained on the COCO dataset. It also uses the
# RoboPiCamContr to command a Lego Mindstorms EV3 robot. 
#
# File: roboPiCamMain.py
# Author: Detlef Heinze 
# Version: 1.1    Date: 27.07.2019       
###########################################################

from tkinter import *
import time 
from PIL import Image, ImageTk
import  roboPiCamContr as RPCC_Contr

#Settings
#Size of picture displayed on the screen
imageDisplaySize= (300, 300)
# Disconnected mode for test purposes
bluetothDiconected = False

#IDs of objects of interest to be detected
#for this application. 43 = bottle, 52 = apple in COCO-Dataset
objectIdsOfInterest = { 43, 52} 

#Terminate program
def terminate():
    print("Program terminates")
    camera.close()
    appWin.destroy()

#Add a rectangle on canvas with object label
def addRectangles(canvas, label, box):
    canvas.create_rectangle(box[0], box[1],
                            box[2], box[3],
                            width=2, outline='yellow')
    canvas.create_text((box[0],box[1]), text= label,
             fill='yellow', anchor=SW)
    
#Handle window close event   
def on_closing():
    print("\nWindow closed by user")
    terminate()

#Create controller and warm up cam
print('RoboPiCam Application 1.0\n')
rpcc= RPCC_Contr.RoboPiCamContr(btDisconMode= bluetothDiconected)   #Step 1
camera= rpcc.configurePiCam()       #Step 3
count=0 #Count processed images

#Create main application window:    #Step 5
appWin = Tk()
appWin.wm_title("RoboPiCam 1.0")
lblPicTaken= Label(appWin, text="Last picture taken")
canPict = Canvas(appWin, height=imageDisplaySize[1],
                         width= imageDisplaySize[0])
lblPicTaken.pack(anchor=W, pady=5)
canPict.pack(fill=X)
appWin.protocol("WM_DELETE_WINDOW", on_closing)

#Check bluetooth connection to EV3
btOK = rpcc.bluetoothStartTest() #Step 6


#Start main loop of application
timeout = time.time() + rpcc.appDuration
processingOK= True  #True if no error occurs in processResult

if btOK:
    print('\nApplication starts...\n')
    while time.time() < timeout and processingOK:
        picData= rpcc.takePhoto()    #Step 8
        #Display image on screen     #Step 10
        img= Image.frombytes('RGB', (picData.shape[1],picData.shape[0]),
                                     picData.astype('b').tostring())
        actPhoto= ImageTk.PhotoImage(image=img)
        canPict.create_image(0,0,image=actPhoto, anchor=NW)
        
        #Run neural network on Edge TPU Accelerator
        result= rpcc.predict(picData)       #Step 11
        detectedObjects= rpcc.analyseResult(result, objectIdsOfInterest) #Step 13
        for obj in detectedObjects:         #Step 15
            addRectangles(canPict, obj[0], obj[1])
        appWin.update()
        processingOK= rpcc.processResult(detectedObjects) #Step 16
        count += 1
    if processingOK:
        print("\nDuration of running application has been reached.")
        print("Duration: ", rpcc.appDuration, "seconds.")
    else:
        print("\nStop with error during processing results")
    print("Number of processed images: ", count)    
terminate()

