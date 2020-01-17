#Update motor code to the one inside the bot

#INPUT NUMBER CODE OF OBSTCLE













#!/usr/bin/python
# adapted from  
 # https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
  # https://github.com/makepluscode/jetson-nano-basic/blob/master/003-control-gpio/test-l298n-ena.py
   # https://www.jonwitts.co.uk/archives/896


import sys, termios, tty, os
import RPi.GPIO as GPIO
import time
import jetson.inference
import jetson.utils

import argparse
import sys
# for right Motor on ENA
ENA = 33
IN1 = 35
IN2 = 37

# for left motor
IN3 = 21
IN4 = 22

# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# initialize EnA, In1, In2, In3, In4 
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)


 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 

#Time of manual control to be active
button_delay = 0.2






















#
# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
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
#


# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
						   formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage())

parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 
parser.add_argument("--camera", type=str, default="0", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")
parser.add_argument("--width", type=int, default=1280, help="desired width of camera stream (default is 1280 pixels)")
parser.add_argument("--height", type=int, default=720, help="desired height of camera stream (default is 720 pixels)")

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
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
	
	#If imput is found then:

    if (char == "p"):
        print("Stop!")
        GPIO.output(ENA, GPIO.LOW)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        exit(0)
 
    if (char == "a"):
        print("Left pressed")
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        time.sleep(button_delay)
 
    elif (char == "d"):
        print("Right pressed")
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        time.sleep(button_delay)
 
    elif (char == "w"):
        print("Up pressed")
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.HIGH)
        time.sleep(button_delay)
 
    elif (char == "s"):
        print("Down pressed")
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        time.sleep(button_delay)














	#If input is not found then taka a camera fram for Object ditection

	# capture the image
	img, width, height = camera.CaptureRGBA()

	# detect objects in the image (with overlay)
	detections = net.Detect(img, width, height, opt.overlay)

# print the detections
#print("detected {:d} objects in image".format(len(detections)))

	for detection in detections:
	print(detection)

	# render the image
	display.RenderOnce(img, width, height)

	# update the title bar
	display.SetTitle("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

# print out performance info
#net.PrintProfilerTimes()











	#If detected Obsticle, then turn back and left

	if (detection == #INPUT NUMBER CODE OF OBSTCLE):
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        time.sleep(button_delay/2)
	#Turn left
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        time.sleep(button_delay)


	#If bottle is detected then go left if bottle is to the left of the center 
	# and go right if the bottle is to the right of the center
	elif (detection == #INPUT NUMBER CODE OF OBSTCLE):

		if (detection.center < 540): # go little left and then forward
       		 GPIO.output(IN1, GPIO.LOW)
       		 GPIO.output(IN2, GPIO.HIGH)
      		  GPIO.output(IN3, GPIO.HIGH)
      		  GPIO.output(IN4, GPIO.LOW)
      		  time.sleep(button_delay/2)
       		 GPIO.output(IN1, GPIO.HIGH)
       		 GPIO.output(IN2, GPIO.HIGH)
       		 GPIO.output(IN3, GPIO.HIGH)
       		 GPIO.output(IN4, GPIO.HIGH)
      		 time.sleep(button_delay)
	

		if (detection.center > 540): # go little right and then forward
       		 GPIO.output(IN1, GPIO.HIGH)
      		  GPIO.output(IN2, GPIO.LOW)
      		  GPIO.output(IN3, GPIO.LOW)
      		  GPIO.output(IN4, GPIO.HIGH)
      		  time.sleep(button_delay/2)
       		 GPIO.output(IN1, GPIO.HIGH)
       		 GPIO.output(IN2, GPIO.HIGH)
       		 GPIO.output(IN3, GPIO.HIGH)
       		 GPIO.output(IN4, GPIO.HIGH)
      		 time.sleep(button_delay)
