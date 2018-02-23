from simpleOSC import initOSCClient, sendOSCMsg
import time

ip = "127.0.0.1"
port = 9002

initOSCClient(ip, port)

sendOSCMsg("/vol", [0.05])
sendOSCMsg("/bypass", [0])
sendOSCMsg("/roomsize", [0.0])

c_arp = [261.63, 329.63, 392.00, 523.25]

i=3
j=0
while(1):
  sendOSCMsg("/freq", [c_arp[i]])
  sendOSCMsg("/bang", [1])
  j += 0.1
  sendOSCMsg("/roomsize", [j]) 
  i =  (i-1)
  if (i < 0):
    i = 3
  if (j > 1.0):
    j = 0.0
  time.sleep(1.0)
