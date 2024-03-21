###

# Umbral de voltaje para detectar ruido
threshold = 1900    # mV

# Variables globales
start_time = 0
group_id = 0

sample_rate = 44100  # Frecuencia de Muestreo
sample_period_ms = 1 / sample_rate  # periodo de muestreo
recording_duration = 5000 # milisegundos
total_samples = 0
total_voltage = 0

def start_recording():
    global start_time, group_id, total_samples, total_voltage
    start_time = utime.ticks_ms()
    group_id += 1
    total_samples = 0
    total_voltage = 0
    lcd.clear()
    lcd.set_cursor(0, 0)
    lcd.print("Grabando: Grupo {}".format(group_id))
    print("Recording started")  # Checkpoint

def stop_recording():
    global group_id, total_samples, start_time
    filename = "/sd/noise-{}-{}-{}.csv".format(utime.localtime()[3], utime.localtime()[4], utime.ticks_diff(utime.ticks_ms(), start_time) / 1000)
    group_id += 1
    print("Recording stopped")  # Checkpoint
    actual_sample_rate = total_samples / (utime.ticks_diff(utime.ticks_ms(), start_time) / 1000)
    lcd.set_cursor(0, 1)
    lcd.print("Sample Rate:{:.2f}Hz".format(actual_sample_rate))

def record_sample():
    global total_samples, total_voltage
    voltage = adc.read_uv() / 1000
    time_ms = utime.ticks_diff(utime.ticks_ms(), start_time) / 1000
    total_samples += 1
    total_voltage += voltage
    avg_voltage = total_voltage / total_samples
    lcd.set_cursor(0, 2)
    lcd.print("Avg Voltage:{:.2f} mV".format(avg_voltage))
    with open(filename, 'a') as f:
        f.write(','.join(str(x) for x in [time_ms, voltage, group_id]) + '\n')
    if total_samples >= recording_duration * sample_rate:
        stop_recording()

# Bucle principal
start_noise_time = None
while True:
    voltage = adc.read_uv() / 1000
    if voltage > threshold:
        if start_noise_time is None:
            start_noise_time = utime.ticks_ms()
        elif utime.ticks_diff(utime.ticks_ms(), start_noise_time) >= 1000:  # 1 segundo
            filename = "/sd/noise-{}-{}-{}.csv".format(utime.localtime()[3], utime.localtime()[4], group_id)
            try:
                os.stat(filename)
            except OSError:
                start_recording()
            start_record_time = utime.ticks_ms()
            while utime.ticks_diff(utime.ticks_ms(), start_record_time) < recording_duration:
                record_sample()
                utime.sleep_us(round(sample_period_ms))  # Espera para lograr frecuencia de muestreo
            stop_recording()
            start_noise_time = None  # Reset the start noise time
    else:
        start_noise_time = None  # Reset the start noise time
        utime.sleep_ms(10)
