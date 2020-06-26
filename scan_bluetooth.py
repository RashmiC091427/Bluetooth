#This script scans nearby bluetooth devices
#It can also be used to return the mac address of the device in search
from bluetooth import *

def scan_devices():
	#Scanning all the nearby available bluetooth devices
	nearby_devices = discover_devices(lookup_names = True)
	return nearby_devices

#request_device: Name of the desired device user wishes to search. ex:"Honor 9 Lite"
def check_device(request_device):
	nearby_devices = discover_devices(lookup_names = True)
	#Check if the user provided device is in the available devices
	#If yes then respective address of the device is returned else none is returned
	for addr, name in nearby_devices:
		k = False
		if request_device.lower() in name.lower():
			k = True
			return addr
