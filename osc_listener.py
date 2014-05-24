#PYTHOSC OSC LISTENER (AKA OSC SERVER)

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import re
import struct

datagramlist = ''

class EchoUDP(DatagramProtocol):
    
    def datagramReceived(self, data, address):
        global datagramlist
        datagramlist = data
        
        #Int is first 4 bytes. Combine, unpack, and remove from the datagram.
        def unpackInt(datagram):
            global datagramlist
            packedInt = datagram[0]
            for num in range(1,4):
                packedInt = packedInt + datagram[num]
            intValue = struct.unpack(">i", packedInt)
            print "Unpacked Integer:", intValue #output is tuple
            datagramlist = datagramlist.replace(datagramlist[0:4],'')
        
        #Similar to unpackInt. Combines, unpacks, and then removes from datagram    
        def unpackFloat(datagram):
            global datagramlist
            packedFloat = datagram[0]
            for num in range(1,4):
                packedFloat = packedFloat + datagram[num]
            floatValue = struct.unpack(">f", packedFloat)
            print "Unpacked Float:", floatValue #output is tuple
            datagramlist = datagramlist.replace(datagramlist[0:4],'')

        def unpackString(datagram):
            global datagramlist
            print "unpacking string"
            newstring = ''
            for x in range(0, len(datagram)):
                if datagram[x] != "\0":
                    newstring = newstring + datagram[x]
                else:
                    stringLen = len(newstring)
                    paddedStringLen = 4-stringLen%4
                    print "UNPACKED STRING:", newstring
                    datagramlist = datagramlist.replace(datagramlist[0:paddedStringLen+stringLen],'')
                    break
        
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
                    print "INT TYPE FOUND AT", num
                    numberOfInts = numberOfInts + 1
                    unpackInt(datagramlist)
                if searchOscTypetag[num] == 'f':
                    print "FLOAT TYPE FOUND AT", num
                    numberOfFloats = numberOfFloats + 1
                    unpackFloat(datagramlist)
                if searchOscTypetag[num] == 's':
                    print "STRING TYPE FOUND AT", num
                    numberOfStrings = numberOfStrings + 1
                    unpackString(datagramlist)
        

def main():    
    reactor.listenUDP(8009, EchoUDP())
    reactor.run()
    
if __name__ == '__main__':
    main()
    