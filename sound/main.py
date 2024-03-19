import os, network, utime, sdcard

from constants import *
from machine import I2C, SoftSPI, ADC
from lcd_i2c import LCD


# WIFI Init
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID,PASS)

# LCD Init
i2c = I2C(0,scl=SCL_LCD,sda=SDA_LCD,freq=FREQ_LCD)
lcd = LCD(addr=I2C_ADDR,cols=COLS_LCD,rows=ROWS_LCD,i2c=i2c)
lcd.begin()
lcd.clear()

# SDCard Init
spi = SoftSPI(1,mosi=MOSI_SD,miso=MISO_SD,sck=SCK_SD)
sd = sdcard.SDCard(spi,CS_SD)

# ADC Init
adc = ADC(MIC_PIN)
adc.atten(ADC.ATTN_6DB)
adc.width(ADC.WIDTH_12BIT)
adc.init()

def measure():
    return adc.read_uv()

def main():
    while True:
        lcd.set_cursor(0,0)
        lcd.print("Sound lvl in mV")
        lcd.set_cursor(0,1)
        lcd.print("Attenuation: 6dB")
        lcd.set_cursor(6,3)
        lcd.print(str(1650-(measure()/1000)))
        utime.sleep(0.12)

main()
