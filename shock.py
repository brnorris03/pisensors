# MQTT
import sensor

# Shock sensor
import RPi.GPIO as GPIO

class ShockSensor(sensor.Sensor):
	def __init__(self):
		super(ShockSensor, self).__init__()
		GPIO.setmode(GPIO.BCM)
		self.SHOCK_PIN = 17
		GPIO.setup(self.SHOCK_PIN, GPIO.IN)

	def get_value(self):
		# The vibration sensor is 1 when no vibration is detected, and 0 when there is vibration
		for i in range(0,windowsize):
	        shock=GPIO.input(SHOCK_PIN)
			if not shock: return 1 
		return not shock

def get_shock2():
	v=1
	for i in range(0,windowsize):
		v = random.randint(1, 10)
	return v

while True:
	s=get_shock2()          
	(result,mid)=mqttc.publish("sensors/newpipe",s,2)
	time.sleep(1)

mqttc.loop_stop()
mqttc.disconnect()

def publish():
	#s = get_shock()
	s = "testing shock"
	publish.single('sensors/newpipe', payload=s, qos=1, hostname='brix.d.cs.uoregon.edu', port='8100' )