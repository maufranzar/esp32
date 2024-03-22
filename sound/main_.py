# main.py

import utime
import array

# Variables globales
BUFFER_SIZE = 512  # Tamaño del buffer igual al tamaño del bloque de la SD
voltages = []
times = []

def sample():
    start_time = utime.ticks_us()
    voltage = adc.read_uv() // 1000  # Convertir a milivoltios
    time = utime.ticks_diff(utime.ticks_us(), start_time)
    return voltage, time  # mV , us

def save_sd():
    global voltages, times
    buf_v = array.array("H", voltages)  # Convertir los datos a array de enteros de 16 bits
    buf_t = array.array("H", times)  # Convertir los datos a array de enteros de 16 bits
    sd.writeblocks(0, buf_v)  # Escribir los datos de voltaje en la SD
    sd.writeblocks(len(buf_v) * 512, buf_t)  # Escribir los datos de tiempo en la SD después de los datos de voltaje
    voltages = []
    times = []


def loop():
    global voltages, times
    count = 0
    start_time = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start_time) < 1000:
        voltage, time = sample()
        voltages.append(voltage)
        times.append(time)
        count += 1
        if len(voltages) >= BUFFER_SIZE:
            save_sd()
            voltages = []
            times = []
    print("Frecuencia de muestreo: {} Hz".format(count))

# Llamada al bucle principal
while True:
    loop()
