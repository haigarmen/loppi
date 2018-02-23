import OSC
from OSC import OSCBundle
import time
import math

client = OSC.OSCClient()
send_address = '127.0.0.1', 9002
recieve_address = '127.0.0.1', 9001
client.connect( send_address )
#s = OSC.OSCServer( recieve_address )
#s.addDefaultHandlers()

def makeMsg(address, content):
    msg = OSC.OSCMessage()
    msg.setAddress(address)
    msg.append(content)
    return msg


t = 0
m = 0
while 1:
    room = 0.5
    volume = 0.5 + 0.5*math.sin(t)
    n =  math.floor(t) - 11
    freq = math.pow(2, n/12)*440
    
    msg1 = makeMsg("/vol", volume)
    msg2 = makeMsg("/freq", freq)
    msg3 = makeMsg("/bang", 1)
    msg4 = makeMsg("/room", room)
    print m

    client.send(msg1)
    client.send(msg2)
    client.send(msg4)
    if (m == 20):
        client.send(msg3)
        m = 0
    t = t  +0.01
    m = m+1
    time.sleep(0.04)
   
