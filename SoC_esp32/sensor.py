import utime
import dht
from record import writer
from variables import *
from check import init_csv
from machine import I2C, Pin
from lcd_i2c import LCD

dht11 = dht.DHT11(DHT11_PIN)
i2c = I2C(0, scl=SCL_LCD, sda=SDA_LCD, freq=FREQ_LCD)
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
lcd.begin()


def read_sensor():
    while True:
        try:
            dht11.measure()
        except OSError as e:
            lcd.set_cursor(0, 1)
            lcd.print(f"Sensor ocupado")
            utime.sleep(2)  # Espera 2 segundos antes de intentar de nuevo
        else:
            lcd.set_cursor(0, 1)
            lcd.print("Lectura correcta")
            temp = dht11.temperature()
            hum = dht11.humidity()
            time = utime.time()

            if temp is not None and hum is not None:
                return time, temp, hum
    
    

def write_csv(time:int, temp:int, hum:int):
    mode = init_csv()

    try:
        with open(RECORD_PATH, mode) as f:
            write_row = writer(f)
            if mode == 'w':
                write_row(["time", "temperature", "humidity"])
            write_row([time, temp, hum])
            lcd.set_cursor(0,3)
            lcd.print("Escritura correcta")
    except OSError as e:
        lcd.set_cursor(0,3)
        lcd.print("Error de escritura")