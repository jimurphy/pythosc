import socket
import re

UDP_IP = "127.0.0.1"
UDP_PORT = 8009

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

typeTagRegex = re.compile('\,[\S]*?\\0')
addressRegex = re.compile('\/[\S]*?\,')

while True:
    data, addr = sock.recvfrom(1024)
       
    print "received message", data
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
    
    