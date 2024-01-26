from machine import Pin

# LCD_I2C: 2004A-v1
I2C_ADDR = 0x27
NUM_ROWS = 4
NUM_COLS = 20
FREQ_LCD = 800000
SCL_LCD = Pin(22)
SDA_LCD = Pin(21)

# MicroSD Card
SCK_SD = Pin(14)
MOSI_SD = Pin(12)
MISO_SD = Pin(13)
CS_SD = Pin(27)

# DHT11
DHT11_PIN = Pin(15)

# BH1750
BH1750_ADDR = 0x23
SDA_BH1750 = Pin(16)
SCL_BH1750 = Pin(4)

# WS2812
LED_PIN = Pin(17,Pin.OUT)

# HCSR04
TRIGGER_PIN = Pin(18, Pin.OUT)
ECHO_PIN = Pin(19, Pin.IN)

# RELE
RELE_A = Pin(25,Pin.OUT)
RELE_B = Pin(26,Pin.OUT)

# SD RECORD
RECORD_NAME = 'record.csv'
RECORD_PATH = '/sd/record.csv'

# WIFI
SSID = 'MAU'
PSWD = 'Hakanamatata00,'
