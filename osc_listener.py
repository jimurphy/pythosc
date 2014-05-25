import socket
import re
import struct
import threading

datagramlist = ''
messageContents = []

UDP_IP = "127.0.0.1"
UDP_PORT = 8009

def datagramReceived(data):
    global datagramlist
    global messageContents
    datagramlist = data
    messageContents = []

    #Int is first 4 bytes. Combine, unpack, and remove from the datagram.
    def unpackInt(datagram):
        global datagramlist
        global messageContents
        packedInt = datagram[0]
        for num in range(1,4):
            packedInt = packedInt + datagram[num]
        intValue = struct.unpack(">i", packedInt)
        print "Unpacked Integer:", intValue #output is tuple
        messageContents.append(intValue)
        datagramlist = datagramlist.replace(datagramlist[0:4],'')
    
    #Similar to unpackInt. Combines, unpacks, and then removes from datagram    
    def unpackFloat(datagram):
        global datagramlist
        global messageContents
        packedFloat = datagram[0]
        for num in range(1,4):
            packedFloat = packedFloat + datagram[num]
        floatValue = struct.unpack(">f", packedFloat)
        print "Unpacked Float:", floatValue #output is tuple
        messageContents.append(floatValue)
        datagramlist = datagramlist.replace(datagramlist[0:4],'')

    def unpackString(datagram):
        global datagramlist
        global messageContents
        stringValue = ''
        for x in range(0, len(datagram)):
            if datagram[x] != "\0":
                stringValue = stringValue + datagram[x]
            else:
                stringLen = len(stringValue)
                paddedStringLen = 4-stringLen%4
                print "Unpacked String:", stringValue
                datagramlist = datagramlist.replace(datagramlist[0:paddedStringLen+stringLen],'')
                break
        messageContents.append(stringValue)

    
    numberOfInts = 0
    numberOfFloats = 0
    numberOfStrings = 0
                    
    typeTagRegex = re.compile('\,[\S]*?\0') #Not sure why these need
    addressRegex = re.compile('\/[\S]*?\,')  #to be compiled every time...

    matchOscAddress = re.match(addressRegex, datagramlist, flags=0)

    searchOscTypetag = re.search(typeTagRegex, datagramlist, flags=0)

    if matchOscAddress:
        matchOscAddress = re.sub(',','',matchOscAddress.group())
        print "Address: ",matchOscAddress
        datagramlist = datagramlist.replace(matchOscAddress, '')
    
    if searchOscTypetag:
        searchOscTypetag = searchOscTypetag.group()
        print "Typetag: ", searchOscTypetag
        typeTagLength = (len(searchOscTypetag) - 1) #Accounts for comma(??)
        datagramlist = datagramlist[(typeTagLength+(4-typeTagLength%4)):]
        for num in range(0, typeTagLength):
            if searchOscTypetag[num] == 'i':
                numberOfInts = numberOfInts + 1
                unpackInt(datagramlist)
            if searchOscTypetag[num] == 'f':
                numberOfFloats = numberOfFloats + 1
                unpackFloat(datagramlist)
            if searchOscTypetag[num] == 's':
                numberOfStrings = numberOfStrings + 1
                unpackString(datagramlist)
        print "MESSAGE CONTENTS", messageContents     
              
class listenForOSC (threading.Thread):
    def __init__(self, threadID, name, port):
        print "TEST"        
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.port = port
    def run(self):
        print "Starting OSC Listener:", self.name
        #instantiate OSC listener class here
        startOSCListener(self.name, self.port)
        print "Exiting thread..."
              
def startOSCListener(threadName, port):
    print "Should start here with port", port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))    
    
    while True:
            data, address = sock.recvfrom(1024) #Pretty sure this blocks until RX
            print "MESSAGE RX"
            datagramReceived(data)        