# MQTT
import paho.mqtt.client as mqtt
import time
import random

class SensorClient:
	def __init__(self, host="iot.eclipse.org", port=1883):
		self.mqttc=mqtt.Client()
		self.mqttc.connect(host,port,60)
		self.mqttc.loop_start()

	def get_value(self):
		# Default fake sensor input; replace with actual sensor values
		# Should return a string
		v=1
		for i in range(0,1000):
			v = random.randint(1, 10)
			if v == 8: return v
		return v

	def run(self):
		while True:
			s=self.get_value()          
			(result,mid)=self.mqttc.publish("sensors/newpipe",s,2)
			time.sleep(1)
		
		self.mqttc.loop_stop()
		self.mqttc.disconnect()

def main():
	sc = SensorClient()
	sc.run()
	
if __name__ == "__main__":
	main()