import config as c
import RPi.GPIO as GPIO
import pyrebase

Ventilateur_GPIO = 11
Buzzer_GPIO = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup( Ventilateur_GPIO ,GPIO.OUT)
GPIO.setup( Buzzer_GPIO ,GPIO.OUT)


firebase = pyrebase.initialize_app(c.config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(c.mail,c.password)

# Get a reference to the database service
db = firebase.database()



def stream_handler_Ventilateur(message):
    Ventilateur = bool(int(str(message['data'][0])))
    GPIO.output( Ventilateur_GPIO , Ventilateur )
    print ("Ventilateur : {}".format(Ventilateur))
my_stream = db.child("Controle/Ventilateur").stream(stream_handler_Ventilateur)



def stream_handler_Buzzer(message):
    Buzzer = bool(int(str(message['data'][0])))
    GPIO.output( Buzzer_GPIO , Buzzer )
    print ("Buzzer : {} ".format(Buzzer))
my_stream = db.child("Controle/Buzzer").stream(stream_handler_Buzzer)
