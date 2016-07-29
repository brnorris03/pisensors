import paho.mqtt.client as mqtt

msg="Initialized MQTT connection"

def start_mqtt():
    client = mqtt.Client("pipe_pub")
    client.connect("brix.d.cs.uoregon.edu",8100,60)
    client.on_connect = on_connect
    client.loop_forever()
    return client

def on_connect(client, userdata, rc):
    print("Connected with result code " + str(rc))
    if rc != 0: 
        client.reconnect()
        
def send_msg(client, userdata, flags, rc):
    global msg
    print("in send_msg")
    client.publish("sensors/newpipe", msg)

def end_mqtt(client):
    client.disconnect()
