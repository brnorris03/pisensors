import paho.mqtt.client as mqtt

def start_mqtt():
  client = mqtt.Client("shock_pub")
  client.connect_async("brix.d.cs.uoregon.edu",8100)
  client.loop_start()
  return client

def send_msg(client, msg):
  client.publish("sensor/shock", msg)

def end_mqtt(client):
  client.disconnect()
