# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import os, utime, ntptime, sdcard

from constants import *
from machine import I2C, SoftSPI, ADC
from lcd_i2c import LCD


# ADC Init
adc = ADC(MIC_PIN)

# LCD Init
i2c = I2C(0,scl=SCL_LCD,sda=SDA_LCD,freq=FREQ_LCD)
lcd = LCD(addr=I2C_ADDR,cols=COLS_LCD,rows=ROWS_LCD,i2c=i2c)
lcd.begin()

# SDCard Init
spi = SoftSPI(1,mosi=MOSI_SD,miso=MISO_SD,sck=SCK_SD)
sd = sdcard.SDCard(spi,CS_SD)
fs = os.VfsFat(sd)
os.mount(fs, '/sd')



def main():
    
    lcd.clear()
    lcd.set_cursor(0,0)
    lcd.print("Ruido en dB: ")


main()