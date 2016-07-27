#!/usr/bin/env python
import time, datetime, os
import grovepi
import mqttutils


debug = False

# Connect the Grove Loudness Sensor to analog port A0
# SIG,NC,VCC,GND
loudness_sensor = 0    # A0

# Accelerometer is plugged into one of the I2C ports, address is 0x6a, check with "sudo i2cdetect -y 1"
#import lsm303d
#try: 
#	acc_mag=lsm303d.lsm303d()
#except IOError:
#	print("Unable to read from accelerometer, check the sensor and try again")

# 3-axis digital accelerometer 16g at address 53
from adxl345 import ADXL345

adxl345 = ADXL345()
print("ADXL345 on address 0x%x:" % (adxl345.address))

# Shock sensor 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
SHOCK_PIN = 17
GPIO.setup(SHOCK_PIN, GPIO.IN)

from netifaces import interfaces, ifaddresses, AF_INET
address = ifaddresses('wlan0').setdefault(AF_INET, [{'addr':'No IP addr'}])[0]['addr']
import grove_rgb_lcd 
grove_rgb_lcd.setText("%s" % address)
print("%s Sensors starting up" % datetime.datetime.now().isoformat())

while True:
    try:
        # Read the sound level
        loudness = grovepi.analogRead(loudness_sensor)
        #if debug: print("loudness sensor value =", loudness)

	# Get accelerometer values
	if False:  # disable because always returns 0
		acc=acc_mag.getRealAccel()
		# Read the heading (6-axis accelerometer/gyro)
		heading= acc_mag.getHeading()
		if debug: print("Acceleration of X,Y,Z is %.3fg, %.3fg, %.3fg" %(acc[0],acc[1],acc[2]))
		if debug: print("Heading %.3f degrees\n" %(heading))

	# 3-axis accel 
	axes = adxl345.getAxes(True)
	#if debug: print(( axes['x'] ),"\t",( axes['y'] ),"\t",( axes['z'] ))

	# Shock sensor
	shock=GPIO.input(SHOCK_PIN)
	tstamp = datetime.datetime.now().isoformat()
        msg = "%s: shock=%d;loudness=%d;accel=%.3f,%.3f,%.3f" % (tstamp, shock, loudness, axes['x'], axes['y'], axes['z']) 

	debugmsg = "sh=%d;loud=%d\n%.1f,%.1f,%.1f" %(shock, loudness, axes['x'], axes['y'], axes['z'])
	if debug: print("Sending MQTT message: %s" % msg)
	grove_rgb_lcd.setText("%s\n%s" % (address,tstamp))
        time.sleep(.3)
	grove_rgb_lcd.setText(debugmsg)
        time.sleep(.3)
        os.system('mosquitto_pub -h brix.d.cs.uoregon.edu -p 8100 -t sensors/pipe -m "%s"' % msg)

    except IOError:
        print "%s Error reading one or more sensor values" % datetime.datetime.now().isoformat()
    except KeyboardInterrupt:
  	if debug: print("Quitting")
	print("%s Sensors stopping" % datetime.datetime.now().isoformat())
  	GPIO.cleanup()
  	mqttutils.stop_mqtt(client)



