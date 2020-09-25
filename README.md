# About

The aim is to replace the Meade LX-6 hand controller with a Raspberry Pi, allowing for remote control of the telescope.
The repository contains the schematics and PCB layout for a simple Pi add-on board and the software to control the
telescope.

# Hardware
## Prerequisites

* A Raspberry Pi 1B or newer, with network connection.

* LX6 control board

* 40-pin Raspberry Pi GPIO connector cable

## Features
The board is based on the 74165 parallel-serial converter, just as the real LX6 hand controller. It supports the main
features of the LX6 controller: east/west movement (RA), north/south movement (dec), 2x-8x speed control and focus
control. It also has the ability to control the shutter of an external DSLR, although no focus control is provided.

The camera control line uses an optocoupler separate from the LX6 circuitry to isolate the camera. The camera's own
power source operates the shutter.

The RJ-45 connector on tbe board connects to the controller DIN-8 plug in the telescope's base. Connect the board to the
Raspberry Pi with the 40-pin GPIO cable. Start the control application on the Pi, then turn on the telescope.

***Caveat #1***: the current design is a bit too simple and does not account for floating inputs (happens when a software
developer is let loose with a soldering iron...) Make sure to start the control program before turning on the telescope.

***Caveat #2***: the board supports switching the telescope's tracking speed between quartz drive and manual control.
However, it is not possible to define the manual speed.

***Caveat #3***: the DSLR control works as-is with a Canon EOS 350D. Some modifications may be needed for other makes
and models. To that end, the board connector is a generic 3-pin header. To prevent wake-up issues, set the camera to
not go in power saving mode between exposures.

* python3.5 (3.5 is the version on Stretch)

`sudo aptitude install python3`

* python3-pyqt5

`sudo aptitude install python3-pyqt5`

* xauth (in order to use X11 forwarding)

`sudo aptitude install xauth`

The installation of pyQt5 may install a large number of dependencies. (Up to 430MB on install.) Be sure to have enough
room on the SD card.

It is not practically possible to use a virtual environment on Raspbian Stretch. Pre-compiled packages are not available
as the ARM architecture is not officially supported and the GCC version included with Stretch fails to compile the
Qt5 source. (Any version of PyQt 5.7 onward triggers a compiler bug.)

## Installation
`git clone https://github.com/scoenye/py_lx6.git`

## Remote access

* Linux

Connect to the Raspberry Pi desktop using VNC/RDP, or forward the X11 display using ssh -X

* Windows

Connect to the Raspberry desktop using VNC/RDP

## Usage

1. `cd` to the installation directory

2. start the application:

`python3 py_lx6.py`

The application has two main control panels. The main panels are selected with buttons in the toolbar. The default panel
emulates the LX6 hand controller. It has toggle buttons for the speed and drive controls and press & hold buttons for
the movement and focus controls. This manual control panel also hosts the single exposure camera control button, The
automation panel provides for predefined scripted control.

Current automation controls:

* Align: implementation of D.A.R.V. (Drift Align method by Robert Vice.) This combines the drift alignment method with
a DSLR to align the telescope. This control has one parameter - the number of seconds to advance the telescope
in RA in one direction (so the total drift window is 2x the parameter value.)
* Unguided exposure: execute a predefined number of long-term exposures. This control has two parameters - the number
of exposures to make, and the duration (seconds) of each exposure. The minimum exposure time is 1 second. For shorter
exposures, use the single exposure button on the manual control panel and the DSLR's own exposure controls.

# License
Distributed under the GNU GPL v3. See LICENSE.txt for more information

# Contact
Sven Coenye - scoenye@compaqnet.be
Project link: [https://github.com/scoenye/py_lx6](URL)

# Acknowledgemets
gEDA for the tools to develop the LX6 control board
