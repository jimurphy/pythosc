from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import re

class EchoUDP(DatagramProtocol):
    
    def datagramReceived(self, data, address):
        typeTagRegex = re.compile('\,[\S]*?\\0')
        addressRegex = re.compile('\/[\S]*?\,')

        matchOscAddress = re.match(addressRegex, data, flags=0)
        searchOscTypetag = re.search(typeTagRegex, data, flags=0)
        
        if matchOscAddress:
            matchOscAddress = re.sub(',$','',matchOscAddress.group())
            print "Address: ",matchOscAddress
        
        if searchOscTypetag:
            searchOscTypetag = re.sub('^,','',searchOscTypetag.group())
            print "Typetag: ", searchOscTypetag
            typeTagLength = (len(searchOscTypetag)-1)
            print typeTagLength
            #if string[i] = s,
            for num in range(0, typeTagLength):
                if searchOscTypetag[num] == 'i':
                    print "INT TYPE FOUND AT", num
                elif searchOscTypetag[num] == 'f':
                    print "FLOAT TYPE FOUND AT", num
                elif searchOscTypetag[num] == 's':
                    print "STRING TYPE FOUND AT", num

def main():    
    reactor.listenUDP(8009, EchoUDP())
    reactor.run()
    
if __name__ == '__main__':
    main()
    