#!/usr/bin/env python2




#MIT License

#Copyright (c) [2020] [Mattias Rexby]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.




# adapted from

# Copyright (c) 2019, NVIDIA CORPORATION.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.



 # https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py

   # https://github.com/makepluscode/jetson-nano-basic/blob/master/003-control-gpio/test-l298n-ena.py

    # https://www.jonwitts.co.uk/archives/896





#import required packages

import sys
import os
import termios
import tty
import RPi.GPIO as GPIO
import time
import jetson.inference
import jetson.utils
import argparse


#turn GPIO warnings off, some thimes when running multiple times one can get som warning notifications, ignore.
GPIO.setwarnings(False)


# set motor pint using board markings any GIPO will do i use the ones set in the demo.

# for right Motor
ENA = 37
IN1 = 35
IN2 = 33

# for left motor
IN3 = 23
IN4 = 24

 

# set pin numbers to the board's

GPIO.setmode(GPIO.BOARD)

 
# initialize EnA, In1, In2, In3, In4

GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

 

 #Manual controll whit keybord, get's a char from keybord imput
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


#IMPORTANT changing width and height will make you in need to changing object detection prtameters on rows 350 and onwards.
# parse the command line - part of the object detection program. Used to set optional parameters like width and height of camera pichure

parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.",

  formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage())

parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")

parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")

parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")

parser.add_argument("--camera", type=str, default="0", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")

parser.add_argument("--width", type=int, default=1280, help="desired width of camera stream (default is 1280 pixels)")

parser.add_argument("--height", type=int, default=720, help="desired height of camera stream (default is 720 pixels)")



 

#Time of manual control to be active, the program is usind delays so to small numbers will make the bot seam to hack when driving, to large will make it go to far befour taking a new detection pichure. 

button_delay = 0.8 #How long the motors are driven befour repeating code
auto_turn_delay =  10 #How long the turns on autopilot to be befour taking a new pichure (it is a divider of button delay)

 

 

try:
    opt = parser.parse_known_args()[0]
except:
    parser.print_help()
    sys.exit(0)

 

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create the camera and display

camera = jetson.utils.gstCamera(opt.width, opt.height, opt.camera)

display = jetson.utils.glDisplay()



# process frames until user exits

while display.IsOpen():

 

#Looks for keybord imput

    char = getch()


#uncomment to use autopilot function "only goes forward"
    #Autopilot
    #print("Looking for item")	
  #  GPIO.output(IN1, GPIO.HIGH)
  #  GPIO.output(IN2, GPIO.HIGH)
  #  GPIO.output(IN3, GPIO.HIGH)
 #   GPIO.output(IN4, GPIO.HIGH)




#If imput is found then from get char:

#char "p" stops the code execution: turns motors off and turns camera off, cleans upp GPIO.
    if (char == "p"):

      print("Stop!")
      GPIO.output(ENA, GPIO.LOW)
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.LOW)
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.LOW)
      GPIO.cleanup()
      exit(0)


#Goes left and then turns motors off as a safety measure, can be removed but be careful
    if (char == "a"):

      print("Left pressed")
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.HIGH)
      time.sleep(button_delay)
      GPIO.output(ENA, GPIO.HIGH)
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.LOW)
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.LOW)



#Goes right and then turns motors off as a safety measure, can be removed but be careful
    elif (char == "d"):

      print("Right pressed")
      GPIO.output(IN3, GPIO.HIGH)
      GPIO.output(IN4, GPIO.LOW)
      time.sleep(button_delay)
      GPIO.output(ENA, GPIO.HIGH)
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.LOW)
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.LOW)



#Goes forward and then turns motors off as a safety measure, can be removed but be careful
    elif (char == "w"):

      print("Up pressed")
      GPIO.output(IN3, GPIO.HIGH)
      GPIO.output(IN4, GPIO.LOW)
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.HIGH)
      time.sleep(button_delay)
      GPIO.output(ENA, GPIO.HIGH)
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.LOW)
    	GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.LOW)

 
 
 
 
#Goes bakwards and then turns motors off as a safety measure, can be removed but be careful
    elif (char == "s"):

      print("Down pressed")
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.HIGH)
      GPIO.output(IN1, GPIO.HIGH)
      GPIO.output(IN2, GPIO.LOW)
      time.sleep(button_delay)
      GPIO.output(ENA, GPIO.HIGH)
      GPIO.output(IN1, GPIO.LOW)
      GPIO.output(IN2, GPIO.LOW)
      GPIO.output(IN3, GPIO.LOW)
      GPIO.output(IN4, GPIO.LOW)

 
 

# capture the image

    img, width, height = camera.CaptureRGBA()


# detect objects in the image (with overlay)

    detections = net.Detect(img, width, height, opt.overlay)

 
    for detection in detections:
        #set detection centerpoint and check ID class of object    
        DetectedCenter = detection.Center[0]
        ClassID = detection.ClassID


 #IMPORTANT this setings handel the object detection set the number of the object you want to detect below ClassID can be set for multiple objects i've set for CandyNet change for other networks
 
 #If there is a obstcle
    # backup and go left
        if (ClassID == 100): 

          print("Going around")
          GPIO.output(IN1, GPIO.LOW)
          GPIO.output(IN2, GPIO.LOW)
          GPIO.output(IN3, GPIO.LOW)
    	    GPIO.output(IN4, GPIO.LOW)
          time.sleep(button_delay / auto_turn_delay)
          GPIO.output(IN1, GPIO.HIGH)
          GPIO.output(IN2, GPIO.HIGH)
          GPIO.output(IN3, GPIO.HIGH)
          GPIO.output(IN4, GPIO.HIGH)
          time.sleep(button_delay)


 

#If object is detected then go left if objcet is to the left of the center
# and go right if the bottle is to the right of the center

        elif (ClassID == 0): #INPUT NUMBER-CODE OF OBJECT TO BE FOLLOWED
     print("Candy!")	

	#Detecting object on the right side of the screen
            if(DetectedCenter < 640): # go little to the left and then forward

              print("Going left") 
              GPIO.output(IN1, GPIO.LOW)
              GPIO.output(IN2, GPIO.HIGH)
              time.sleep(button_delay / auto_turn_delay)
              GPIO.output(ENA, GPIO.HIGH)
       	      GPIO.output(IN1, GPIO.LOW)
       	      GPIO.output(IN2, GPIO.LOW)
       	      GPIO.output(IN3, GPIO.LOW)
       	      GPIO.output(IN4, GPIO.LOW)
              break


 
	#Detecting object on the right side of the screen
            elif (DetectedCenter > 640): # go little to the right and then forward
              print("Going right")
              GPIO.output(IN3, GPIO.HIGH)
              GPIO.output(IN4, GPIO.LOW)
              GPIO.output(IN4, GPIO.LOW)
              time.sleep(button_delay*4/ auto_turn_delay)
              GPIO.output(ENA, GPIO.HIGH)
       	      GPIO.output(IN1, GPIO.LOW)
       	      GPIO.output(IN2, GPIO.LOW)
       	      GPIO.output(IN3, GPIO.LOW)
       	      GPIO.output(IN4, GPIO.LOW)
              break

 

    # render the image

    display.RenderOnce(img, width, height)

 


