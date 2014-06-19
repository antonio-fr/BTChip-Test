"""
*******************************************************************************    
*   BTChip Bitcoin Hardware Wallet Python Test Interface
*
*   (c) 2014 Antoine FERRON
*   
*  This program is free software: you can redistribute it and/or modify
*  it under the terms of the GNU General Public License as published by
*  the Free Software Foundation, version 3 of the License.
*  This program is distributed in the hope that it will be useful,
*  but WITHOUT ANY WARRANTY; without even the implied warranty of
*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*  GNU General Public License for more details.
*  You should have received a copy of the GNU General Public License
*  along with this program.  If not, see <http://www.gnu.org/licenses/>

********************************************************************************
"""
from btchip import *

class UserBTChip(btchip):
	def close(self):
		self.dongle.close()
	
	def exchange(self,intr,p1,p2,lenout,params=None):
		apdu = [ self.BTCHIP_CLA, intr, p1, p2, lenout ]
		if params!=None:
			apdu.append(len(params))
			apdu.extend(params)
		return self.dongle.exchange(bytearray(apdu))
	
	def getversion(self):
		return self.exchange(self.BTCHIP_INS_GET_FIRMWARE_VERSION,0,0,5)
	
	def disp_version(self):
		resp = self.getversion()
		version = ".".join([ str((resp[1]<<8)+resp[2]), str(resp[3]), str(resp[4]) ] )
		print "Firmware version :",version 
		print "Using compressed keys :",
		if resp[0] == 0x01: print "Yes"
		else: print "No"
	
	def getmode(self):
		return self.exchange(self.BTCHIP_INS_GET_OPERATION_MODE,0,0,1)
	
	def disp_mode(self):
		resp = self.getmode()
		print "Mode enabled:",
		respi=ord(resp)
		if respi&0x01: print "standard wallet"
		if respi&0x02: print "relaxed wallet"
		if respi&0x04: print "server"
		if respi&0x08: print "developer"
		if respi&0x80: print "forward setup"

try:
	mydongle = UserBTChip(getDongle())
except:
	print "No dongle can be accessed!"
	quit()
print "\nDongle BTChip detected\n"

mydongle.disp_version()
mydongle.disp_mode()

pin = raw_input("Enter PIN:")
try:
	mydongle.verifyPin(pin)
except:
	print "Wrong PIN !"
	quit()
print "PIN OK"

print "Please Wait..."
adr = mydongle.getWalletPublicKey( 2, 1, 1)['address']
print "First Address is", adr

mydongle.close()

