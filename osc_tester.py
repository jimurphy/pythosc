from time import time, sleep
import osc_sender

def sendOsc():
    sender1 = osc_sender.OSCClient("127.0.0.1", 8009)
    sender1.SetAddress("/test/message")
    sender1.SetTypetag("s")
    
    #sender1.AddString("")
    #sender1.AddFloat(69.5)
    sender1.AddString("YOLO")
    sender1.Transmit()

while True:
    sendOsc()
    sleep(1)    