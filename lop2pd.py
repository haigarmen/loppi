#!/usr/bin/python

import os        # import os for sending messages to PD
import spidev    # import the spidev module
import time      # import time for the sleep function
import RPi.GPIO as GPIO

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

waitTime = .05
bounceTime = 0.01

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
def send2Pd(message=''):
    # Send a message to Pd
    os.system("echo '" + message + ";' | pdsend 3000")

def readadc(channel):
    if channel > 7 or channel < 0:
        return -1

    # spi.xfer2 sends three bytes and returns three bytes:
    # byte 1: the start bit (always 0x01)
    # byte 2: configure bits, see MCP3008 datasheet table 5-2
    # byte 3: don't care
    r = spi.xfer2([1, 8 + channel << 4, 0])

    # Three bytes are returned; the data (0-1023) is in the
    # lower 3 bits of byte 2, and byte 3 (datasheet figure 6-1)
    v = ((r[1] & 3) << 8) + r[2]

    return v;

while True:
    input_right = GPIO.input(4)
    input_left = GPIO.input(17)
    input_down = GPIO.input(18)
    input_up = GPIO.input(27)

    values = [0]*9
    
    for i in range(8):
        values[i] = readadc(i)
        message = str(i) + ' ' + str(values[i]) # make a string for use with Pdsend
        send2Pd(message)
    if input_right == False:
#            print('Right Pressed')
        message = '9 1'
        send2Pd(message)
        time.sleep(bounceTime)
    elif input_left == False:
##        print('Left Pressed')
        message = '9 2'
        send2Pd(message)
#        values.insert(8,21)
        time.sleep(bounceTime)
    elif input_down == False:
##        print('Down Pressed')
        message = '9 3'
        send2Pd(message)
#        values.insert(8,31)
        time.sleep(bounceTime)
    elif input_up == False:
##        print('Up Pressed')
#        values.insert(8,41)
        message = '9 4'
        send2Pd(message)
        time.sleep(bounceTime)

# consider creating a message that has all values in one string rather than separate messages
#    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} | {8:>4} |'.format(*values))
#    print(message)
    time.sleep(waitTime)