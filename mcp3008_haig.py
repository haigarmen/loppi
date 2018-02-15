#!/usr/bin/env python

# Written by Haig Armen, altered script by Limor "Ladyada" Fried for Adafruit

import time
import os
import spidev

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts

# Function to calculate temperature from
# TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp(data,places):
 
  # ADC Value
  # (approx)  Temp  Volts
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  465      100    1.50
  #  775      200    2.50
  # 1023      280    3.30
 
  temp = ((data * 330)/float(1023))-50
  temp = round(temp,places)
  return temp

# Define sensor channels
channel_1 = 7
##channel_2  = 1
 
# Define delay between readings
delay = 1
 

while True:
 
  # Read the light sensor data
  adc1_level = ReadChannel(channel_1)
##  1_volts = ConvertVolts(adc1_level,2)
 
  # Read the temperature sensor data
##  temp_level = ReadChannel(temp_channel)
##  temp_volts = ConvertVolts(temp_level,2)
##  temp       = ConvertTemp(temp_level,2)
 
  # Print out results
  print ("--------------------------------------------")
  print("ADC 1: {}".format(adc1_level))
##  print("ADC 1: {} ({}V)".format(adc1_level,1_volts))
##  print("Temp : {} ({}V) {} deg C".format(temp_level,temp_volts,temp))
 
  # Wait before repeating loop
  time.sleep(delay)
