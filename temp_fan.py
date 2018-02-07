import os, sys, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Innentemperatur auslesen

def get_temp_in():
      
# 1-wire Slave Datei lesen
    file = open('/sys/bus/w1/devices/28-000005d2e508/w1_slave')
    filecontent = file.read()
    file.close()
 
# Temperaturwerte auslesen und konvertieren
    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    temperature = float(stringvalue[2:]) / 1000
 
# Temperatur ausgeben
    rueckgabewert = '%6.2f' % temperature 
    return(rueckgabewert)

# Aussentemperatur auslesen

def get_temp_out():
      
# 1-wire Slave Datei lesen
    file = open('/sys/bus/w1/devices/28-000005d2e508/w1_slave')
    filecontent = file.read()
    file.close()
 
# Temperaturwerte auslesen und konvertieren
    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    temperature = float(stringvalue[2:]) / 1000
 
# Temperatur ausgeben
    rueckgabewert = '%6.2f' % temperature 
    return(rueckgabewert)

# Setting the GPIO-pin for the relay output

pinList = [17]

# loop through pins and set mode and state to 'high'

for i in pinList:   
  GPIO.setup(i, GPIO.OUT)   
  GPIO.output(i, GPIO.HIGH)  

# Starting the loop.

while True:
	temp_in = get_temp_in( )
	temp_out = get_temp_out( )

# Telling the program to turn on the fan only if the inside temperature is above the specified value.

	if temp_in >= 5.5:

# Telling the program to compare the temperatures of the two sensors and to turn off the fan if the inside temperature is lower than the outside temperature and to turn it on in the other case.

		if temp_in <= temp_out:
			print("off")
			GPIO.output(17, GPIO.HIGH)
			time.sleep(5)
		else:
			print("on")
			GPIO.output(17, GPIO.LOW)
			time.sleep(5)

# Telling the program to turn off the fan if the inside temperature is below the specified value.

	if temp_in <=4:
		print("off")
		GPIO.output(17, GPIO.HIGH)
		time.sleep(5)