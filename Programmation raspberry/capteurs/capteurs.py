import pyrebase
import time
import DHT
import config as c
import RPi.GPIO as GPIO

LDR_GPIO = 37
PIR_GPIO = 12
DHT_GPIO = 8
MQ5_GPIO = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup( LDR_GPIO ,GPIO.IN)
GPIO.setup( PIR_GPIO ,GPIO.IN)
GPIO.setup( MQ5_GPIO,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


instance = DHT.DHT11(pin = 8)



firebase = pyrebase.initialize_app(c.config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(c.mail,c.password)

# Get a reference to the database service
db = firebase.database()


def CalcTemp():
        while True :
                result = instance.read()
                Temp = result.temperature
                if ( Temp > 0 ) :
                        return Temp
                        break


def CalcHum():
        while True :
                result = instance.read()
                Hum = result.humidity
                if ( Hum > 0 ) :
                        return Hum
                        break


        
while True :
        LDR = str(int(GPIO.input(LDR_GPIO)))
        PIR = str(int(GPIO.input(PIR_GPIO)))
        MQ5 = str(int(GPIO.input(MQ5_GPIO)))
        Temperature = CalcTemp()
        Humidite = CalcHum()
        print("LDR : {} ".format(LDR))
        print("PIR : {}".format(PIR)) 
        print ("MQ5 : {}".format(MQ5))
        print ("Temperature : {}".format(Temperature))
        print ("Humidite : {}".format(Humidite))
        Capteurs = {'Gaz':MQ5,'PIR':PIR,'LDR':LDR,'Humidite':Humidite,'Temperature':Temperature}
        db.child("Capteurs").update(Capteurs)
        time.sleep(0.5)
    
   

