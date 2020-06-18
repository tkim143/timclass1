#Class libraries for the bluetooth application
#using time
import time #<----class library. 1st party

from bluetooth.ble import BeaconService
#beacon service is a 3rd party module

service = BeaconSerice() #creating an instance object of the class library

service.start_advertising("11111111-2222-3333-4444-5555555555555", 1, 1, 1, 2000) #advertise the uuid and different ports for spoofing devices


time.sleep(15) #every 15 seconds
service.stop_advertise()

print("Done.")