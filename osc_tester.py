from time import time, sleep
import osc_sender

def sendOsc():
    sender1 = osc_sender.OSCClient("127.0.0.1", 8009)
    sender1.SetAddress("/test/message")
    sender1.SetTypetag("issif")
    
    sender1.AddInt(77)
    sender1.AddString("The quick brown fox")
    sender1.AddString("jumped o'er the lazy God!!")
    sender1.AddInt(100)
    sender1.AddFloat(3.14159)
    
    sender1.Transmit()

while True:
    sendOsc()
    sleep(1)