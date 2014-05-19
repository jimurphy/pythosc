from time import time, sleep
import osc_sender

def sendOsc():
    sender1 = osc_sender.OSCClient("127.0.0.1", 8009)
    sender1.SetAddress("/test/message")
    sender1.SetTypetag("iiiiii")
    
    sender1.AddInt(77)
    sender1.AddInt(222)
    sender1.AddInt(666)
    sender1.AddInt(111)
    sender1.AddInt(2)
    sender1.AddInt(23)
    
    #sender1.AddInt(333)
    
    sender1.Transmit()

while True:
    sendOsc()
    sleep(1)    