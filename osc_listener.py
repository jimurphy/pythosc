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
        print "DATAGRAMLIST", datagramlist
        def unpackInt(position, datagram):
            global datagramlist
            packedInt = datagram[0]
            for num in range(1,4):
                packedInt = packedInt + datagram[num]
            intValue = struct.unpack(">i", packedInt)
            print "Unpacked Integer:", intValue #output is tuple
            datagramlist = datagramlist.replace(datagramlist[0:4],'')
            
        def unpackFloat(position, datagram):
            print "unpacking float at position", position

        def unpackString(position, datagram):
            print "unpacking string at position", position
            nullRegex = re.sub(r',','',datagram) #Remove comma
            nullRegex = re.sub(r'\0{1,}','/',nullRegex) #Many nulls to one slash
            oscValues = nullRegex.split("/") # /x/y/z into [x, y, z]
            del oscValues[0] # Unsure why.
            
            stringValue = oscValues[position]
            print "STRING VALUE AT ", position, ":", stringValue
        
        numberOfInts = 0
        numberOfFloats = 0
        numberOfStrings = 0
                        
        typeTagRegex = re.compile('\,[\S]*?\\0') #Not sure why these need
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
            typeTagLength = (len(searchOscTypetag))
            print typeTagLength
            datagramlist = datagramlist[(typeTagLength+(4-typeTagLength%4)):]
            for num in range(0, typeTagLength):
                if searchOscTypetag[num] == 'i':
                    print "INT TYPE FOUND AT", num
                    numberOfInts = numberOfInts + 1
                    unpackInt(num, datagramlist)
                if searchOscTypetag[num] == 'f':
                    print "FLOAT TYPE FOUND AT", num
                    numberOfFloats = numberOfFloats + 1
                    #unpackFloat(num, datagramlist)
                if searchOscTypetag[num] == 's':
                    print "STRING TYPE FOUND AT", num
                    numberOfStrings = numberOfStrings + 1
                    #unpackString(num, datagramlist)
        

def main():    
    reactor.listenUDP(8009, EchoUDP())
    reactor.run()
    
if __name__ == '__main__':
    main()
    