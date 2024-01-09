import utime
import dht
from record import writer
from variables import *
from check import init_csv
from machine import I2C, SoftI2C
from lcd_i2c import LCD

dht11 = dht.DHT11(DHT11_PIN)
i2c_bh1750 = SoftI2C(scl=SCL_BH1750, sda=SDA_BH1750,freq=400000)
i2c = I2C(0, scl=SCL_LCD, sda=SDA_LCD, freq=FREQ_LCD)
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
lcd.begin()


def read_bh1750():
    
    i2c.writeto(BH1750_ADDR, b'\x10')
    utime.sleep(1)    
    data = i2c.readfrom(BH1750_ADDR, 2)
    light = ((data[0] << 8) | data[1]) / 1.2

    return light
    

def read_sensor():
    while True:
        try:
            dht11.measure()
            utime.sleep(0.5)
        except OSError as e:
            lcd.set_cursor(0, 1)
            lcd.print(f"Sensor ocupado")
            utime.sleep(1)  # Espera 2 segundos antes de intentar de nuevo
        else:
            lcd.set_cursor(0, 1)
            lcd.print("Lectura correcta")
            temp = dht11.temperature()
            hum = dht11.humidity()
            light = read_bh1750()
            time = utime.time()

            if temp is not None and hum is not None and light is not None:
                return time, temp, hum, light
    
    

def write_csv(time:int, temp:int, hum:int, light:float):
    mode = init_csv()

    try:
        with open(RECORD_PATH, mode) as f:
            write_row = writer(f)
            if mode == 'w':
                write_row(["time", "temperature", "humidity", "light"])
            write_row([time, temp, hum, light])
            lcd.set_cursor(0,2)
            lcd.print("Escritura correcta")
    except OSError as e:
        lcd.set_cursor(0,2)
        lcd.print("Error de escritura")

