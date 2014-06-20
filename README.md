BTChip-Test
===========
Copyright (C) 2014  Antoine FERRON

Basic test samples for BTChip API in python
-------------------------------------------

This is a basic test sample for BTChip-API in Python

BTChip-API is documented here:
http://btchip.github.io/btchip-doc/bitcoin-technical.html


Needed for BTChip-Test:
-----------------------
All you need is **BTChip-python**
https://github.com/btchip/btchip-python

But that requires:
**PyUSB** v1.0 http://downloads.sourceforge.net/project/pyusb/PyUSB%201.0/1.0.0-alpha-2/pyusb-1.0.0a2.zip
( python 2.7 needed )

PyUSB requires **libusb**
  
  
  
- For **Windows** :

1) install LibUsb-win32
http://downloads.sourceforge.net/project/libusb-win32/libusb-win32-releases/1.2.6.0/libusb-win32-bin-1.2.6.0.zip
Mainly, you need to copy dll in system windows file (Read http://pastebin.com/raw.php?i=e3AHMUDR)

2) Zadig
http://zadig.akeo.ie/downloads/zadig_2.1.0.exe
or XP version : http://zadig.akeo.ie/downloads/zadig_xp_2.1.0.exe  
Connect BTCHip  
Launch Zadig  
Install libusb-win32 driver for "Plug-up" device  

3) Install PyUSB  
Get PyUSB zip upper  
unzip and launch in cmd (in unzipped folder)  
```setup.py install```  
  
  
  
- For **Linux** :

1) Install libusb from your package manager

2) Install PyUSB  
Get PyUSB zip upper  
unzip and launch in console (in dir unzipped)  
  
```python2.7 setup.py install```


Use BTChip-Test :
-----------------
Copy main.py of this soft in btchip-python/btchip folder  
(folder get from btchip-python-master in github link upper)  
Launch "main.py"  
Enter PIN when prompted  


Licence :
----------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
