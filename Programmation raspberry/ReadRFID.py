import RPi.GPIO as GPIO
import MFRC522python.SimpleMFRC522
import time
import config as c
import json

RFID_Users = dict()
GPIO.setwarnings(False)

def CheckUser(i):
	i = str(i)
	detected = False
	global  RFID_Users
	with open('Configuration/RFIDUser.json','r') as f:
		RFID_Users = json.load(f)
	for k,v  in RFID_Users.items():
		if ( k == i):
			detected = True
                        print ("hello {}".format(RFID_Users[i]))
			break
			
	return detected	

while True:
        reader = MFRC522python.SimpleMFRC522.SimpleMFRC522()

# try:
	id, text = reader.read()
	print(id)
	if (CheckUser(id) == True):
		print ("open door")
		time.sleep(1)
#        print(text)
#        except:
#                pass
#        finally:
#                GPIO.cleanup()


