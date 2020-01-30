import pyrebase
import time
import config as c
import smbus


firebase = pyrebase.initialize_app(c.config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(c.mail,c.password)

# Get a reference to the database service
db = firebase.database()

# i2c address of PCF8574
PCF8574=0x24

# open the bus (0 -- original Pi, 1 -- Rev 2 Pi)
b=smbus.SMBus(1)

# make certain the pins are set high so they can be used as inputs
b.write_byte(PCF8574, 0xff)


def decodeI2cPCF(val):
	SwitchAdmin =   val & 0b00000001
	SwitchEntre = ( val & 0b00000010) >> 1
	SwitchInterieur  = ( val & 0b00000100) >> 2
	return SwitchAdmin , SwitchEntre , SwitchInterieur

while True:
	val = b.read_byte(PCF8574)
	S1 = decodeI2cPCF(val)[0]
	S2 = decodeI2cPCF(val)[1]
	S3 = decodeI2cPCF(val)[2]
	print (" Etat SwitchAdmin  : {}".format(S1))
	print (" Etat SwitchEntre  : {}".format(S2))
	print (" Etat SwitchInterieur  : {}".format(S3))
	data = {'SwitchAdmin': S1 , 'SwitchEntre': S2 , 'SwitchInterieur': S3 }
	db.child("Capteurs/SwitchEtat").update(data)
	time.sleep(1)



