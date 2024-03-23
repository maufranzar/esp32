# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import machine,os,network,utime,sdcard,webrepl,struct

from constants import *
from machine import I2C, SPI, ADC
from lcd_i2c import LCD


# LCD Init
i2c = I2C(0,scl=SCL_LCD,sda=SDA_LCD,freq=FREQ_LCD)
lcd = LCD(addr=I2C_ADDR,cols=COLS_LCD,rows=ROWS_LCD,i2c=i2c)
lcd.begin()
lcd.clear()
print("LCD initialized")  # Checkpoint
lcd.set_cursor(0, 0)
lcd.print("LCD            OK")
utime.sleep_ms(1000)


# SDCard Init (v2)
spi = SPI(1,mosi=MOSI_SD,miso=MISO_SD,sck=SCK_SD)
sd = sdcard.SDCard(spi,CS_SD)
spi.init(baudrate=20_000_000)
# fs = os.VfsFat(sd)

print("SDCard initialized")  # Checkpoint
lcd.set_cursor(0, 1)
lcd.print("SDCard         OK")
utime.sleep_ms(1000)


# WIFI Init
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID,PASS)
print("WiFi initialized")  # Checkpoint
lcd.set_cursor(0, 2)
lcd.print("WiFi           OK")
utime.sleep_ms(1000)

# ADC Init
adc = ADC(MIC_PIN)
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
adc.init()
print("Sensor initialized")  # Checkpoint
lcd.set_cursor(0, 3)
lcd.print("Sensor         OK")
utime.sleep_ms(1000)


while station.isconnected() == False:
    lcd.clear()
    lcd.set_cursor(0, 2)
    lcd.print("Linking...")
    utime.sleep_ms(100)
    
else:
    ip_address = station.ifconfig()[0]
    lcd.clear()
    lcd.set_cursor(0, 0)
    lcd.print("webREPL Conectado:")
    lcd.set_cursor(0, 1)
    lcd.print(ip_address+":8266")
    webrepl.start()

    
for i in range(9,-1,-1):
    lcd.set_cursor(0, 2)
    lcd.print("Iniciando en {}s".format(i))
    utime.sleep_ms(1000)

