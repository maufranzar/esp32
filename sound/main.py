# main.py

BUFFER_SIZE = 4096
BLOCK_SIZE = 512
BLOCKS_IN_BUFFER = BUFFER_SIZE // BLOCK_SIZE

buffer = bytearray(BUFFER_SIZE)
buffer_index = 0
block_num = 0

# Función para obtener una muestra
def sample():
    start_time = utime.ticks_us()
    voltage = adc.read()  # 12-bit ADC - 3.3v
    timestamp = utime.ticks_diff(utime.ticks_us(), start_time)    
    data = struct.pack('HH', timestamp, voltage)  # a binario
    return data

def data_into_buffer(data):
    global buffer_index
    buffer[buffer_index:buffer_index + 4] = data
    buffer_index += 4

def save_buffer():
    global buffer, buffer_index, block_num

    for i in range(BLOCKS_IN_BUFFER):
        start = i * BLOCK_SIZE
        end = (i + 1) * BLOCK_SIZE
        sd.writeblocks(block_num + i, buffer[start:end])

    block_num += BLOCKS_IN_BUFFER
    buffer_index = 0

def main_loop():
    global buffer, buffer_index

    loop_count = 0
    start_time = utime.ticks_ms()

    while utime.ticks_diff(utime.ticks_ms(), start_time) < 1000:
        data = sample()
        data_into_buffer(data)

        if buffer_index >= BUFFER_SIZE:
            save_buffer()

        loop_count += 1

    print(f"Frequency: {loop_count}Hz")
    lcd.clear()
    lcd.print("Frequency: {}Hz".format(loop_count))

### Main ###

start = utime.ticks_ms()
while utime.ticks_diff(utime.ticks_ms(), star) < 5_000:
    main_loop()