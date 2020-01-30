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

def stream_handler_Mode(message):
    Mode = db.child("Mode").get().val()
    with open('Configuration/Mode.json','w') as f:
        json.dump(Mode,f)
    print (Mode)
my_stream = db.child("Mode").stream(stream_handler_Mode)

def stream_handler_Consigne(message):
    Consigne = db.child("Consigne").get().val()
    with open('Configuration/Consigne.json','w') as f:
        json.dump(Consigne,f)
    print (Consigne)
my_stream = db.child("Consigne").stream(stream_handler_Consigne)

def stream_handler_RFID(message):
        RFIDUser = db.child("Login/RFID").get().val()
        with open('Configuration/RFIDUser.json','w') as f:
                json.dump(RFIDUser,f)
        print (RFIDUser)
my_stream = db.child("Login/RFID").stream(stream_handler_RFID)


def stream_handler_Keypad(message):
        KeypadPass = {'KeypadPass': message['data']}
        with open('Configuration/KeypadPass.json','w') as f:
                json.dump(KeypadPass,f)
        print (KeypadPass)
my_stream = db.child("Login/Keypad").stream(stream_handler_Keypad)

