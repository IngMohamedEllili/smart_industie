import pyrebase
import time
import config as c
import RPi.GPIO as GPIO


LampeAdmin_GPIO = 35
LampeEntre_GPIO = 29
LampeInterne_GPIO = 31
LampEXT_GPIO = 33 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup( LampeAdmin_GPIO  ,GPIO.OUT)
GPIO.setup( LampeEntre_GPIO  ,GPIO.OUT)
GPIO.setup( LampeInterne_GPIO  ,GPIO.OUT)
GPIO.setup( LampEXT_GPIO ,GPIO.OUT)

firebase = pyrebase.initialize_app(c.config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(c.mail,c.password)

# Get a reference to the database service
db = firebase.database()



def stream_handler_Lampes(message):
	LampsChild2GPIO(message) 
my_stream = db.child("Controle/Lampes").stream(stream_handler_Lampes)

def stream_handler_LampExt(message):
	LampExt2GPIO(message)
my_stream = db.child("Controle/LampeExt").stream(stream_handler_LampExt)

def LampsChild2GPIO(message):
	data = db.child('Controle/Lampes').get().val()
	LampeAdmin = bool(int(data['LampeAdmin']))
	LampeEntre = bool(int(data['LampeEntre']))
	LampeInterne = bool(int(data['LampeInterne']))
	print ("LampeAdmin :  {} ".format(LampeAdmin))
	print ("LampeEntre :  {} ".format(LampeEntre))
	print ("LampeInterne  :  {} ".format(LampeInterne))
	GPIO.output( LampeAdmin_GPIO , LampeAdmin )
	GPIO.output( LampeEntre_GPIO , LampeEntre )
	GPIO.output( LampeInterne_GPIO , LampeInterne )

def LampExt2GPIO(message):
	LampExt = bool(int(message['data']))
	print ("LampExt :  {} ".format(LampExt))
	GPIO.output( LampEXT_GPIO , LampExt )

