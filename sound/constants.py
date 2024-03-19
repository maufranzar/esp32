from machine import Pin

# LCD_I2C: 2004A-v1
I2C_ADDR = 0x27
ROWS_LCD = 4
COLS_LCD = 20
FREQ_LCD = 800000

SDA_LCD = Pin(8)
SCL_LCD = Pin(10)


# MicroSD Card
MISO_SD = Pin(3)
MOSI_SD = Pin(4)
SCK_SD = Pin(2)
CS_SD = Pin(5)

# Neopixel
LED_PIN = Pin(1)

# Max4466
MIC_PIN = Pin(0)

# UART
TX_PIN = Pin(20)
RX_PIN = Pin(21)

#WiFi
SSID = "MAU"
PASS = "Hakanamatata00,"
