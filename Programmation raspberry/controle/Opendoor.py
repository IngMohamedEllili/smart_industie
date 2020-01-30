import RPi.GPIO as GPIO        
import time

ServoPin = 27 
                         
GPIO.setwarnings(False)          
GPIO.setmode (GPIO.BCM)           
GPIO.setup(ServoPin,GPIO.OUT)             
p = GPIO.PWM(ServoPin,50)              
p.start(7.5)                            
                                                                                        
time.sleep(5)                                                     
p.ChangeDutyCycle(2.5)       
time.sleep(1)
