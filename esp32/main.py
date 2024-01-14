import sensor
import check
import utime
import record
from variables import *
from check import last_row
from lcd_i2c import LCD
from machine import I2C

i2c = I2C(0, scl=SCL_LCD, sda=SDA_LCD, freq=FREQ_LCD)
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
lcd.begin()



lcd.set_cursor(0, 0)
lcd.print("Iniciando...")
    

for i in range(82):
    # lectura de datos
    time, temp, hum, light = sensor.read_sensor()
    
    # escritura en el sd
    sensor.write_csv(time,temp,hum,light)
    
    # comprobacion de duplicados
    status = check.data(time,temp,hum,light)
    print(status)
    
    response = None
        
    if  status:
    
        last_data = last_row()
        print(last_data)
        json_data = record.to_json(last_data)
        print(json_data)
        response = record.sent_json(json_data)
        
        if response is not None:
            lcd.set_cursor(0, 3)
            lcd.print("Enviado con exito")
            
        else:
            lcd.set_cursor(0, 3)
            lcd.print("Error de envio")
        
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