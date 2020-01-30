import pyrebase
import sys
from config import *

Nom = sys.argv[1]
Prenom = sys.argv[2]
AdresseEmail= sys.argv[3]
Mot_de_passe = sys.argv[4]

my_dict_inscri = {"Nom":Nom , "Prenom":Prenom , "Email":AdresseEmail,"MDP":Mot_de_passe }



firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(mail, password)

# Get a reference to the database service
db = firebase.database()

db.child("Inscription_Qt").push(my_dict_inscri)
