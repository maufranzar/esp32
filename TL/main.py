from machine import UART
import time

# Ejemplo: Usando UART2 en los pines GPIO17 (TX) y GPIO16 (RX)
uart2 = UART(2, baudrate=115200, tx=17, rx=16)

while True:
    if uart2.any():
        data = uart2.read()  # Lee todos los bytes disponibles
        if data:
            print("Recibido en UART2:", data)
    time.sleep(0.1)
