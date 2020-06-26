#This script scans nearby bluetooth devices
#It can also be used to return the mac address of the device in search
from bluetooth import *

def scan_devices():
	nearby_devices = discover_devices(lookup_names = True)
	return nearby_devices
	
def check_device(request_device):
	#print ("This script scans nearby bluetooth devices. Please wait...")
	nearby_devices = discover_devices(lookup_names = True)
	#print ("Found ",len(nearby_devices)," devices")
	for addr, name in nearby_devices:
		k = False
		if request_device.lower() in name.lower():
			k = True
			return addr
