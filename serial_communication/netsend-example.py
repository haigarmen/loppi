import serial
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BCM)

#set the GPIO input pins
pad0 = 22
pad1 = 27
pad2 = 17
pad3 = 24
pad4 = 18

GPIO.setup(pad0, GPIO.IN)
GPIO.setup(pad1, GPIO.IN)
GPIO.setup(pad2, GPIO.IN)
GPIO.setup(pad3, GPIO.IN)
GPIO.setup(pad4, GPIO.IN)

subprocess.call("pd-extended yourpatch.pd &", shell=True)

pad0alreadyPressed = False
pad1alreadyPressed = False
pad2alreadyPressed = False
pad3alreadyPressed = False
pad4alreadyPressed = False

a = 1
b = 2
c = 3
d = 4
e = 5

def send2Pd(message=''):
    os.system("echo '" + message + "' | pdsend 3000 localhost udp")

while True:
    pad0pressed = not GPIO.input(pad0)
    pad1pressed = not GPIO.input(pad1)
    pad2pressed = not GPIO.input(pad2)
    pad3pressed = not GPIO.input(pad3)
    pad4pressed = not GPIO.input(pad4)
    
    if pad0pressed and not pad0alreadyPressed:
        send2Pd(str(a))
    pad0alreadyPressed = pad0pressed

    if pad1pressed and not pad1alreadyPressed:
        send2Pd(str(b))
    pad1alreadyPressed = pad1pressed

    if pad2pressed and not pad2alreadyPressed:
        send2Pd(str(c))
    pad2alreadyPressed = pad2pressed

    if pad3pressed and not pad3alreadyPressed:
        send2Pd(str(d))
    pad3alreadyPressed = pad3pressed

    if pad4pressed and not pad4alreadyPressed:
        send2Pd(str(e))
    pad4alreadyPressed = pad4pressed

    time.sleep(0.1)
