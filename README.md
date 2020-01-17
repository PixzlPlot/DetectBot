# DetectBot
This little bugger doesn't like bottles.. So he tries to run them over!
The DetectBot is programmed using the pre-made code from the Nvidia Jetson ''Hello world'' there are just a few more installations needed to be done to get it up and running.


Multi object dates from SSD-Mobilenet-v2 using 91-COCO classes or by making your own data set, set parameters for follow and avoid - remote control and video ransfere.


This robot will after being trained be able to go on autopilot/classify objects and when finding present objects it can find and identefy/follow, if the trained network has some problems you can whit a remote PC control the Bot whit a keyboard.


DetectBot can be remotely controlled using any Linux/Windows/Mac PC using noMachine,
for video/keyboard streaming download NoMachine to both PC and Jetson Nano - https://www.nomachine.com/download

### Rationale
Trying to follow the Jebtbot instructions I soon realized that it expected a webcam to be used whit Jupierlab and I were using the MSI camera, furthermore I like to have more control than one gets in Jupiterlab so I decided to do my own project using the Jetson Nano image.

### Instructions
Edit the DetectBot.py text file if you want to change parameters for example key input, objects to detect, turning speed and so on.
You might need to install some packages used in the file, as of now I am unsure what are pre-installed on the Jetson image, if any packages are missing google fror the download and follow instructions to install.
Put the DetectBot. py in your home directory and the run with sudo./DetectBot. py.

	Shortcuts:
	W drive forward
	S drive backward
	A drive left
	D drive right
	P stock program
	Backspace hold down to drive the automatic search and find protocoll

### Setup
Sadly enught i dont have any instructions for asembly, get som double sided adhesive and a screwdriver and you'll be set. Some pichures on the assembeld bot - Note this is not the final product so it is stillin alfa state and looks like this after trial and error.

Go to in to the DetectBot. by file and read from PIN configuration, you can use any GPIO pins for setup however you need to change the numbers accordingly in the DetectBot.py file.

### List of materials

Jetson Nano - https://developer.nvidia.com/buy-jetson

12V UBEC - https://www.banggood.com/DC-DC-Converter-Step-Down-Module-UBEC-3A-5V-12V-BEC-For-RC-Airplane-FPV-p-981978.html?rmmds=myorder

5V UBEC - https://www.banggood.com/DC-DC-Converter-Step-Down-Module-UBEC-3A-5V-12V-BEC-For-RC-Airplane-FPV-p-981978.html?rmmds=myorder

L298N Motor Driver - https://www.banggood.com/Wholesale-L298N-Dual-H-Bridge-Stepper-Motor-Driver-Board-p-42826.html?rmmds=myorder&cur_warehouse=CN

2.1mm contact - https://www.banggood.com/Universal-USB-to-DC-Power-Plug-Cable-5_52_1mm-Adapter-5V-Charging-Wire-For-RC-Model-Monitor-Tablet-p-1412205.html?rmmds=myorder&cur_warehouse=CN

Chassi - https://www.banggood.com/DIY-Aluminous-Smart-RC-Robot-Car-Tank-Chassis-Base-For-Single-Chip-UNO-p-1602880.html?rmmds=myorder&cur_warehouse=CN

DS card 32GB+ - https://www.banggood.com/BlitzWolf-BW-TF1-Class-10-UHS-1-32GB-UHS-3-V30-64GB-128GB-Micro-SD-TF-Memory-Card-with-Adapter-p-1490559.html?rmmds=myorder&ID=43653&cur_warehouse=HK

WiFi modul - https://www.banggood.com/Wareshare-Wireless-Network-Card-Intel-8265AC-8265NGW-2_4G5G-WIFI-bluetooth-4_2-Module-For-Jetson-Nano-p-1526308.html?rmmds=myorder&cur_warehouse=CN

Acrylcase - https://www.banggood.com/Acrylic-Case-Box-with-Cooling-Fan-for-NVIDIA-Jetson-Nano-Developer-Module-Kit-Shell-Enclosure-Cooler-p-1524028.html?rmmds=myorder&ID=6263680&cur_warehouse=CN

IMX219 160 degrees camera - https://www.banggood.com/Wareshare-IMX219-Camera-Module-Applicable-for-Jetson-Nano-77120160200-FOV-8-Megapixels-p-1526258.html?rmmds=myorder&ID=6263684&cur_warehouse=CN

Jumper cables - https://www.banggood.com/40pcs-10cm-Female-To-Female-Jumper-Cable-Dupont-Wire-For-Arduino-p-994059.html?rmmds=myorder&cur_warehouse=CN

Any 3-6S 500-1500mah LIPO battery, examble - https://www.banggood.com/TATTU-22_2V-1300mAh-75C-6S-XT60-Plug-Lipo-Battery-for-FPV-RC-Racing-Drone-p-1512837.html?rmmds=search&cur_warehouse=CN

### Price about 200 USD

