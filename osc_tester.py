from time import time, sleep
import pythonClassTest

def sendOsc():
    sender1 = pythonClassTest.OSCClient("127.0.0.1", 8009)
    sender1.SetAddress("/test/message")
    sender1.SetTypetag("iii")
    
    #sender1.AddString("")
    #sender1.AddFloat(69.5)
    sender1.AddInt(13)
    sender1.Transmit()

while True:
    sendOsc()
    sleep(1)    