#!/usr/bin/python

# Lots of Pots Board Analog to Digital Converter test
# Modern Device
# www.moderndevice.com

import spidev    # import the spidev module
import time      # import time for the sleep function
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

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
    for i in range(8):
#        value = readadc(i)
#        print "%4d" % value,
         values[i] = readadc(i)
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    time.sleep(0.2)
