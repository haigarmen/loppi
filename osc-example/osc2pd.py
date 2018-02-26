import socket
import time

IP="127.0.0.1"
PORT=9000
addr=(IP, PORT)
EOL=';\n'

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    for i in range(10):
        msg="list foo "+str(i)+" bar"
        sock.sendto(msg+EOL, addr)
    time.sleep(1.0)
