import grove_rgb_lcd

from netifaces import interfaces, ifaddresses, AF_INET
address = ifaddresses('wlan0').setdefault(AF_INET, [{'addr':'No IP addr'}])[0]['addr']
#print("%s Sensors starting up" % datetime.datetime.now().isoformat())
grove_rgb_lcd.setText("%s" % address)
messages = []

class displayThread(threading.Thread):
    def __init__(self, threadID, name, delay=1):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        threadLock.acquire()
        self.display()
        # Free lock to release next thread
        threadLock.release()

    def display(self):
	global messages
        global address
	for message in messages:
	    if not message: message = address
            grove_rgb_lcd.setText("%s" %  message)
 	    os.sleep(self.delay)

