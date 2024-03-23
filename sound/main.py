import struct

# Configuración


# Variables
buffer = bytearray(BUFFER_SIZE)
buffer_index = 0
block_num = 0


# Función para obtener una muestra
def sample():
    try:
        start_time = utime.ticks_us()
        voltage = adc.read() # 12-bit ADC - 3.3v
        timestamp = utime.ticks_diff(utime.ticks_us(), start_time)    
        data = struct.pack('HH', timestamp, voltage) # a binario
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None


def data_into_buffer(data):
    global buffer_index
    buffer[buffer_index:buffer_index + 4] = data
    buffer_index += 4

def save_buffer():
    global buffer, buffer_index, block_num

    try:
        for i in range(8):  # Hay siempre 8 bloques en el buffer
            start = i * BLOCK_SIZE
            end = (i + 1) * BLOCK_SIZE
            sd.writeblocks(block_num + i, buffer[start:end])

        block_num += 8  # Incrementar el número de bloque para la próxima escritura
        buffer_index = 0  # Reiniciar el índice del buffer
    except Exception as e:
        print(f"Error: {e}")


def main_loop():
    global buffer, buffer_index

    while True:
        start_time = utime.ticks_us()
        data = sample()

        # Colocar los datos en el buffer
        data_into_buffer(data)

        # Si el buffer está lleno, guardar los datos en la tarjeta SD
        if buffer_index >= BUFFER_SIZE:
            save_buffer()

        time = utime.ticks_diff(utime.ticks_us(), start_time)
        print(f"tiempo: {time} us")

main()