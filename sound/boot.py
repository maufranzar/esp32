# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import os, network, utime, ntptime, sdcard, webrepl

from constants import *
from machine import I2C, SoftSPI
from lcd_i2c import LCD


# WIFI Init
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID,PASS)

# LCD Init
i2c = I2C(0,scl=SCL_LCD,sda=SDA_LCD,freq=FREQ_LCD)
lcd = LCD(addr=I2C_ADDR,cols=COLS_LCD,rows=ROWS_LCD,i2c=i2c)
lcd.begin()

# SDCard Init
spi = SoftSPI(1,mosi=MOSI_SD,miso=MISO_SD,sck=SCK_SD)
sd = sdcard.SDCard(spi,CS_SD)
fs = os.VfsFat(sd)
os.mount(fs, '/sd')


while station.isconnected() == False:
    lcd.set_cursor(0, 0)
    lcd.print("Conectando...")
    
else:
    ip_address = station.ifconfig()[0]
    lcd.clear()
    lcd.set_cursor(0, 0)
    lcd.print("webREPL Conectado:")
    lcd.set_cursor(0, 1)
    lcd.print(ip_address+":8266")
    webrepl.start()

if 'sd' in os.listdir():
    
    lcd.set_cursor(0, 2)
    sd_stat = os.statvfs('/sd')
    lcd.print("SD Card: OK!")
    utime.sleep(2)
    free_space = sd_stat[0]*sd_stat[3]
    lcd.set_cursor(0, 3)
    lcd.print("SD Free:{}MB".format(free_space/1024/1024))
    
    ntptime.settime()
    t = utime.localtime()
    formatted_time = "{:02d}-{:02d}_{:02d}:{:02d}".format(t[1],t[2],t[3],t[4])
    filename = '/sd/boot_log.txt'
    with open(filename, 'a') as file:
        file.write("{},{},{}\n".format(formatted_time,ip_address,free_space))
            
else:
        lcd.set_cursor(0, 2)
        lcd.print("SD Card: Fail!")
        lcd.set_cursor(0, 3)
        lcd.print("Inserte una SD Card!")

    
for i in range(9,-1,-1):
    lcd.set_cursor(0, 2)
    lcd.print("Iniciando en {}s".format(i))
    utime.sleep(1)

