from time import time, sleep

import osc_listener
        
thread1 = osc_listener.listenForOSC(1, "OSC LISTENER", 8009)

try:
    thread1.daemon = True #kills when parents exits. not graceful.
    thread1.start()
except:
    print "ERROR: Can't start OSC Listener Thread..."
    
while True:
    sleep(1.5)
    print "TEST IN MAIN THREAD"