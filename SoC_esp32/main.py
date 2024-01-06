import sensor
import check
import utime
from variables import *
from lcd_i2c import LCD
from machine import I2C

i2c = I2C(0, scl=SCL_LCD, sda=SDA_LCD, freq=FREQ_LCD)
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
lcd.begin()


lcd.set_cursor(0, 0)
lcd.print("Iniciando...")
    

for i in range(82):
    # lectura de datos
    time, temp, hum = sensor.read_sensor()
    
    # escritura en el sd
    sensor.write_csv(time,temp,hum)
    
    # comprobacion de duplicados
    status = check.data(time,temp,hum)
    print(status)

    if  status:
        utime.sleep(10)
        lcd.clear()
        lcd.set_cursor(0, 0)
        lcd.print("Iteracion: {i}".format(i=i))
        continue
    
    else:
        lcd.set_cursor(0, 0)
        lcd.print(f"status: {status}".format(status))
                 
        
lcd.set_cursor(0, 3)
lcd.print("Fin del programa")