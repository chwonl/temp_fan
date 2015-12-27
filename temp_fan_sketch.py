import os
import time

# Getting the temperature of the inside sensor.
def get_temp_in( ):
	temp_in = 6
	return temp_in

# Getting the temperature of the outside sensor.
def get_temp_out( ):
	temp_out= -24
	return temp_out
# Starting the loop.
while True:
	temp_value_in = get_temp_in( )
	temp_value_out = get_temp_out( )

# Telling the program to turn on the fan only if the inside temperature is above the specified value.
	if temp_value_in >= 5.5:

# Telling the program to compare the temperatures of the two sensors and to turn off the fan if the inside temperature is lower than the outside temperature and to turn it on in the other case.
		if temp_value_in <= temp_value_out:
			print("off")
			time.sleep(5)
		else:
			print("on")
			time.sleep(5)

# Telling the program to turn off the fan if the inside temperature is below the specified value.
	if temp_value_in <=4:
		print("off")
		time.sleep(5)
