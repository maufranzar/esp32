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


# RECORD
RECORD_NAME = 'record.csv'
RECORD_PATH = '/sd/record.csv'

# WIFI
SSID = 'MAU'
PSWD = 'Hakanamatata00,'
