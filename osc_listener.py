#PYTHOSC OSC LISTENER (AKA OSC SERVER)

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import re
import struct

class EchoUDP(DatagramProtocol):
    
    def datagramReceived(self, data, address):
        numberOfInts = 0
        numberOfFloats = 0
        numberOfStrings = 0
        
        typeTagRegex = re.compile('\,[\S]*?\0') #Not sure why these need
        addressRegex = re.compile('\/[\S]*?\,')  #to be compiled every time...

        matchOscAddress = re.match(addressRegex, data, flags=0)
        searchOscTypetag = re.search(typeTagRegex, data, flags=0)

        if matchOscAddress:
            matchOscAddress = re.sub(',','',matchOscAddress.group())
            print "Address: ",matchOscAddress
            data = data.replace(matchOscAddress, '')
        
        if searchOscTypetag:
            searchOscTypetag = re.sub(r',','',searchOscTypetag.group())
            print "Typetag: ", searchOscTypetag
            typeTagLength = (len(searchOscTypetag)-1)
            data = data.replace(searchOscTypetag, '')                   
            print typeTagLength
            for num in range(0, typeTagLength):
                if searchOscTypetag[num] == 'i':
                    print "INT TYPE FOUND AT", num
                    numberOfInts = numberOfInts + 1
                    self.unpackInt(num, data)
                elif searchOscTypetag[num] == 'f':
                    print "FLOAT TYPE FOUND AT", num
                    numberOfFloats = numberOfFloats + 1
                    self.unpackFloat(num, data)
                elif searchOscTypetag[num] == 's':
                    print "STRING TYPE FOUND AT", num
                    numberOfStrings = numberOfStrings + 1
                    self.unpackString(num, data)
        
        nullRegex = re.sub(r',','',data) #Remove comma
        nullRegex = re.sub(r'\0{1,}','/',nullRegex) #Many nulls to one slash
        oscValues = nullRegex.split("/") # /x/y/z into [x, y, z]
        del oscValues[0] # Unsure why.
        
        paddedValue = oscValues[2]
        padAmount = 4 - (len(oscValues[2]) % 4)
        paddedValue = ("\0" * padAmount) + paddedValue
        struct.unpack(">i", paddedValue)
        
    def unpackInt(self, position, datagram):
        print "unpacking int at position", position

    def unpackFloat(self, position, datagram):
        print "unpacking float at position", position

    def unpackString(self, position, datagram):
        print "unpacking string at position", position


def main():    
    reactor.listenUDP(8009, EchoUDP())
    reactor.run()
    
if __name__ == '__main__':
    main()
    