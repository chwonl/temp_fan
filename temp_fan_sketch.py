#coding: utf-8
# Title: temp_fan.py
# Author: Christian Wehrli 
# License: GNU GENERAL PUBLIC LICENSE
# Description: This script can be used to blow outside air into a room (e.g. basement) to lower its temperature down to a defined value (e.g. 5° Celsius). A fan is connected to a Raspberry Pi B+ via a relay and is simply turnt on or off. There are two DS18B20 temperature sensors that measure the inside and outside temperatures.


import os
import time
#### import RPi.GPIO as GPIO

# Defining the function to turn the fan ON.
#### def fan_on(pin):
def fan_on():
####	GPIO.output(pin,GPIO.HIGH)
	print("Fan is ON!")
	
# Defining the function to turn the fan ON.	
#### def fan_off(pin):
def fan_off():
####	GPIO.output(pin,GPIO.LOW)
	print("Fan is OFF!")

# Resetting all the GPIOs. All set as input.
#### GPIO.cleanup()

# To use Raspberry Pi board pin numbers.
#### GPIO.setmode(GPIO.BOARD)

# Set up GPIO output channel.
#### GPIO.setup(11, GPIO.OUT)

# Getting the temperature of the inside sensor.
def get_temp_in( ):
 temp_in = 6
 return temp_in
 
# Getting the temperature of the outside sensor.
def get_temp_out( ):
 temp_out= input("Aussentemperatur?")
 return temp_out
# Starting the loop.
while True:
 temp_value_in = get_temp_in( )
 temp_value_out = get_temp_out( )
 
# Telling the program to turn on the fan only if the inside temperature is above the specified value.
 if temp_value_in >= 5.5:
 
# Telling the program to compare the temperatures of the two sensors and to turn off the fan if the inside temperature is lower than the outside temperature and to turn it on in the other case.
  if temp_value_in <= temp_value_out:
####	fan_off(11)
   fan_off()
   time.sleep(5)
  else:
####	fan_on(11)
   fan_on()
   time.sleep(5)
 
# Telling the program to turn off the fan if the inside temperature is below the specified value.
 if temp_value_in <=4:
####	fan_off(11)
  fan_off()
  time.sleep(5)
 
