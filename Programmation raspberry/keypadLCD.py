from pad4pi import rpi_gpio
import time
import I2C_LCD_driver
import json, ast
import subprocess


mylcd = I2C_LCD_driver.lcd()

code = ""
hiddenCode = ""


global  CorrectCode

with open('Configuration/KeypadPass.json','r') as f :

        data = json.load(f)
        global  CorrectCode
        CorrectCode = data['KeypadPass']

# Setup Keypad
KEYPAD = [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"],
        ["*","0","H"]
]

def print_key(key):
	global code
	global hiddenCode
	if(key == "*"):
		global CorrectCode
		if (code == CorrectCode):
			print ("open door")
			code = ""
			hiddenCode = ""
			mylcd.lcd_display_string( "correct" , 1)
			subprocess.Popen(["python3","controle/Opendoor.py"])
			
		else:
			print ("Incorrect")
			code = ""
			hiddenCode = ""
			mylcd.lcd_display_string( "Incorrect" , 1)
	elif (key == "H"):
		code = ""
		hiddenCode = ""
		mylcd.lcd_clear()

	else:
		code = str(code)+(key)
		hiddenCode = hiddenCode + "*"
	mylcd.lcd_display_string( hiddenCode , 1)
	print (code)


COL_PINS = [23,24,4,0] # numerotation BCM
ROW_PINS = [12,16,20,21] # numerotation BCM
factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
keypad.registerKeyPressHandler(print_key)
print("Appuyez sur les boutons de votre clavier. Ctrl+C pour sortir.")
try:
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Goodbye")
finally:
    keypad.cleanup()
