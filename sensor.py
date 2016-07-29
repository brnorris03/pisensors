# MQTT
import paho.mqtt.client as mqtt
import time
import random

class Sensor:
	def __init__(self):
		self.mqttc=mqtt.Client()
		
	def connect(self, host="iot.eclipse.org", port=1883):
		self.mqttc.connect(host,port,60)
		self.mqttc.loop_start()

	def get_value(self):
		'''
			Get the sensor value using specific sensor input mechanism, e.g., GPIO
			@return string value to be sent as MQTT message
		'''
		# Default fake sensor input; replace with actual sensor values
		v=1
		for _ in range(0,1000):
			v = random.randint(1, 10)
			#if v == 8: return v
		return str(v)

	def run(self,delay=1,qos=2):
		while True:
			s=self.get_value()          
			(result,mid)=self.mqttc.publish("sensors/newpipe",s,qos)
			time.sleep(delay)
		
		self.mqttc.loop_stop()
		self.mqttc.disconnect()
		


# For testing only
def main():
	sc = Sensor()
	sc.connect()
	sc.run()  # also disconnects when done
	
if __name__ == "__main__":
	main()