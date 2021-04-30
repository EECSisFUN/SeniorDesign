**Description**

Controller for various Windows functions via external Raspberry Pi w/ touchscreen

Functions including, but not limited to:

* windows audio mix                              -- 90% needs polish -- jace fix
* overworld to switch between apps               -- 90% needs polish -- jace fix
* spotify integration                            -- 100%             -- done
* media mode                                     -- 90%              -- meet
* drawing pad / touch mouse pad (like laptop)    -- 95%              -- apurva
* windows/google calendar integration            -- 0%               -- tri and max
* launch applications                            -- 95%              -- tri pham
* twitch/twitch chat integration                 -- 95%              -- max
* switch desktop/windows                         -- 90% needs polish -- jace fix
* zoom controls                                  -- 0%               -- everyone


**Emulation**

Without a Raspberry Pi with serial cable, you will need to emulate COM ports to develop/test

you can do this with the a null-modem emulator which can be downloaded 

here: https://sourceforge.net/projects/com0com/

Run the x64 or x84 exe (doesnt matter which), tick all boxes and run setup

do not close the program yet

Then open device manager in windows

expand "com0com - serial port emulators"

right click one of the devices and "update drivers"

choose "search automatically for updates"

it should find and update the drivers (it might not, and that is fine)

Then hit the reset button on com0com

The second pair should change "COM#->COM#" to something like "COM3->COM4" (or whatever ports are being used)

to check this, expand "ports(COM & LPT)" in device manager

and check that "com0com - serial port emulator(COM3)" and "com0com - serial port emulator(COM3)" are listed (or whatever ports are being used)

You will need to do this with two connections for two-way emulation so something like "COM3->COM4" and "COM5->COM6" need to be enabled and listed in com0com

whichever ports are enabled in com0com needs to be reflected in the files device/server.py and coms/Main.py

Like in this image:

![image](https://github.com/EECSisFUN/SeniorDesign/blob/master/portExample.png)


**Electron**

Set up the nodejs by running 

`npm install` in the SeniorDesign/device directory

**Python**

To install all imports

`pip3 install -r requirements.txt`

Also note that Microsoft Visual C++ 14.0 build tools are required for pycaw (theycan be installed here: https://visualstudio.microsoft.com/visual-cpp-build-tools/)


