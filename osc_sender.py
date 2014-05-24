import socket
import struct

class OSCClient:    
    IPAddress = "127.0.0.1"
    Port = 8001
    Address = "/test"
    Typetag = "i"
    oscMessage = ""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    typetagLength = 0
    argumentCount = 0
    
    canSend = False
    
    def __init__(self, ip, port):
        self.IPAddress = ip
        self.Port = port
           
    def SetAddress(self, address):
        messageLength = len(address)
        msgAppendAmount = (4-messageLength%4)
        for num in range(0, msgAppendAmount):
           address = address + "\0"
        self.oscMessage = self.oscMessage + address  
           
    def SetTypetag(self, typetag):       
        typetag = "," + typetag
        self.typetagLength = len(typetag)
        typetagAppendAmount = (4-self.typetagLength%4)
        if typetagAppendAmount == 0:
            typetagAppendAmount = 4
        for num in range(0, typetagAppendAmount):
            typetag = typetag + "\0"
        self.oscMessage = self.oscMessage + typetag  
    
    def AddInt(self, int):
        if self.argumentCount < (self.typetagLength - 1):
            int = struct.pack(">i", int)
            self.oscMessage = self.oscMessage + int
            self.argumentCount = 1 + self.argumentCount
            self.canSend = True
        else:
            print "ERROR. Argument count greater than what typetag specifies."
            self.canSend = False
    
    def AddFloat(self, float):
        if self.argumentCount < (self.typetagLength - 1):
            float = struct.pack(">f", float)
            self.oscMessage = self.oscMessage + float
            self.argumentCount = 1 + self.argumentCount            
            self.canSend = True
        else:
            print "ERROR. Argument count greater than what typetag specifies."
            self.canSend = False

    def AddString(self, string):
        stringLength = len(string)
        msgAppendAmount = (4-stringLength%4)
        for num in range(0, msgAppendAmount):
           string = string + "\0"
        self.oscMessage = self.oscMessage + string
        self.canSend = True
        
    def Transmit(self):
        if self.canSend == True:
            self.sock.sendto(bytes(self.oscMessage), (self.IPAddress, self.Port))
            print "Transmitting", self.oscMessage
            self.argumentCount = 0
            self.canSend = False
        else:
            print "ERROR: Can't send. Check argument counts and typetag."
