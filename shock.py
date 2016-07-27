# Shock sensor
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
SHOCK_PIN = 17
GPIO.setup(SHOCK_PIN, GPIO.IN)

def get_shock(windowsize=1000):
 	# The vibration sensor is 1 when no vibration is detected, and 0 when there is vibration
	for i in range(0,windowsize):
        	shock=GPIO.input(SHOCK_PIN)
		if not shock: return 1 
	return not shock

