import pyrebase
import sys
from config import *

Nom = sys.argv[1]
Prenom = sys.argv[2]
N_carte_rfid= sys.argv[3]
Mot_de_passe = sys.argv[4]

my_dict = {"Nom":Nom , "Prenom":Prenom , "N_carte_rfid":N_carte_rfid,"Mot_de_passe :":Mot_de_passe }



firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(mail, password)

# Get a reference to the database service
db = firebase.database()

db.child("employees").push(my_dict)

    
