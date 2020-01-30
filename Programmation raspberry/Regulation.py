import pyrebase
import time
import config as c
import json

firebase = pyrebase.initialize_app(c.config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(c.mail,c.password)

# Get a reference to the database service
db = firebase.database()


def GetModeEclairage():
	with open('Configuration/Mode.json','r') as f :
		Mode = json.load(f)
		return Mode['MEclairage']
        
def GetModeVentilateur():
	with open('Configuration/Mode.json','r') as f :
		Mode = json.load(f)
		return Mode['MVentilateur']
        
def GetTemperatureSeuil():
	with open('Configuration/Consigne.json','r') as f :
		Consigne = json.load(f)
		return Consigne['Temperature']



def stream_handler_capteurs(message):
	Capteurs = db.child("Capteurs").get().val()
	Regulation(Capteurs)
my_stream = db.child("Capteurs").stream(stream_handler_capteurs)

def RegulationTemp(Temp):
	if ( Temp > GetTemperatureSeuil() ) :
		if GetModeVentilateur() == 'Auto' :
			db.child("Controle").update({'Ventilateur':'1'})
	else :                       
		if GetModeVentilateur() == 'Auto' :               
			db.child("Controle").update({'Ventilateur':'0'})

def Regulation(Capteurs):
	if( Capteurs['PIR'] == '1' or Capteurs['Gaz'] == '1' ) :
		db.child("Controle").update({'Buzzer':'1'})
	else :
		db.child("Controle").update({'Buzzer':'0'})
	if ( Capteurs['LDR'] == '1' and GetModeEclairage() == 'Auto' ):
		db.child("Controle").update({'LampeExt':'1'})
	elif ( Capteurs['LDR'] == '0' and GetModeEclairage() == 'Auto' ) :
		db.child("Controle").update({'LampeExt':'0'})
	RegulationTemp(Capteurs['Temperature'])

