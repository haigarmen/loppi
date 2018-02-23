from simpleOSC import initOSCClient, sendOSCMsg
import time

ip = "127.0.0.1"
port = 9002

initOSCClient(ip, port);

sendOSCMsg("/vol", [0.05])
sendOSCMsg("/bypass", [1])
sendOSCMsg("/freq", [440])
sendOSCMsg("/bang", [1])

print "Hellow!"
