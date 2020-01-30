import pyrebase
import time
import os
import subprocess
import config as c

global ActivationSystemeTotale
ActivationSystemeTotale = False

firebase = pyrebase.initialize_app(c.config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(c.mail,c.password)

# Get a reference to the database service
db = firebase.database()
#-------------------------------------------------------------
global procGetConfiguration
global procRFID
global procKeypad
global procRegulation
global procCapteurs
global procEtatLampes
global procLampes
global procControle

#-------------------------------------------------------------
#print ("get configuration")
#procGetConfiguration =subprocess.Popen(["python3","GetConfiguration.py "])
#time.sleep(3)

#-------------------------------------------------------------


def stream_handler_Activation_Systeme_Totale(message):
	SystemeTotal(bool(int(message['data'])))
my_stream = db.child("Activation_Systeme/Activation_Systeme_Total").stream(stream_handler_Activation_Systeme_Totale)

def stream_handler_Activation_Capteurs(message):
	SystemeCapteurs(bool(int(message['data'])))
my_stream = db.child("Activation_Systeme/Activation_Capteurs").stream(stream_handler_Activation_Capteurs)

def stream_handler_Activation_Controle(message):
	SystemeControle(bool(int(message['data'])))
my_stream = db.child("Activation_Systeme/Activation_Controle").stream(stream_handler_Activation_Controle)


def SystemeTotal(boolVar):
	global ActivationSystemeTotale
	if boolVar :
		print ("Activation Systeme_Total")
		ActivationSystemeToltal()
	else :
		print ("Desactivation Systeme_Total")
		DesactivationSystemeToltal()
        
def SystemeCapteurs(boolVar):
	if boolVar :
		print ("Activation Capteurs")
		ActivationCapteurs()
	else :
		print ("Desactivation Capteurs")
		DesactivationCapteurs()

def SystemeControle(boolVar):
	if boolVar :
		print ("Activation Controle")
		ActivationControle()
	else :
		print ("Desactivation Controle")
		DesactivationControle()

def ActivationSystemeToltal():
	global procGetConfiguration
	global procRFID
	global procKeypad
	global procRegulation
	procGetConfiguration = subprocess.Popen(["python3","GetConfiguration.py"])
	procRFID = subprocess.Popen(["python","ReadRFID.py"])
	procKeypad = subprocess.Popen(["python3","keypadLCD.py"])
	procRegulation = subprocess.Popen(["python3","Regulation.py"])

def DesactivationSystemeToltal():
	global procGetConfiguration , procRFID , procKeypad , procRegulation
	if ( procGetConfigurationID ):
		os.system("sudo kill "+str(procGetConfiguration.pid))
		os.system("sudo kill "+str(procRFID.pid))
		os.system("sudo kill "+str(procKeypad.pid))
		os.system("sudo kill "+str(procRegulation.pid))

def ActivationCapteurs():
	global procCapteurs , procEtatLampes
	procCapteurs = subprocess.Popen(["python3","capteurs/capteurs.py"])
	procEtatLampes = subprocess.Popen(["python3","capteurs/EtatLampes.py"])

def DesactivationCapteurs():
	global procCapteurs , procEtatLampes
	os.system("sudo kill "+str(procCapteurs.pid))
	os.system("sudo kill "+str(procEtatLmapes.pid))

def ActivationControle():
	global procLampes , procControle
	procLampes = subprocess.Popen(["python3","controle/lampe.py"])
	procControle = subprocess.Popen(["python3","controle/controle.py"])
    
def DesactivationControle():
	global procLampes , procControle
	os.system("sudo kill "+str(procLampes.pid))
	os.system("sudo kill "+str(procControle.pid)) 

