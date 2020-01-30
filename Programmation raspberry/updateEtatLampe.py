import pyrebase
from config import *


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password ( mail, password )

# Get a reference to the database service
db = firebase.database()


def stream_handler(message):
        UpdateLampeEtat()
my_stream = db.child("Capteur/SwitchEtat").stream(stream_handler)

def stream_handler(message):
        UpdateLampeEtat()      
my_stream = db.child("Controle/Lampes").stream(stream_handler)





def UpdateLampeEtat():
        
        SwitchEtat = db.child("Capteurs/SwitchEtat").get().val()
        ControleLampes = db.child("Controle/Lampes").get().val()
        
        EtatLampeAdmin = db.child("Controle/Lampes/LampeAdmin").get().val() 
        EtatLampeEntre = db.child("Controle/Lampes/LampeEntre").get().val()
        EtatLampeInterieur = Concidence( bool(int(SwitchEtat['SwitchInterieur'])) , bool(int(ControleLampes['LampeInterne'])) )

        EtatLampe = {'EtatLampeAdmin' : str(int(EtatLampeAdmin)) , 'EtatLampeEntre' : str(int(EtatLampeEntre)) , 'EtatLampeInterieur' : str(int(EtatLampeInterieur)) }
        db.child("Capteurs").update({'EtatLampe':EtatLampe})
        
def Concidence(A,B):
        return ( A and B ) or ( ( not A ) and ( not B ))

        


        

