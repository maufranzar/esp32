
sample_freq = 16000
sample_interval = 1 / sample_freq
umbral = 100
tiempo = []
voltaje = []
grupo = 0

def escucha():
    global sample_freq, umbral, grupo, tiempo, voltaje
    start_time = time.ticks_ms()
    while True:
        lectura = adc.read_uv() /1000 # mV
        if lectura > umbral:
            if time.ticks_diff(time.ticks_ms(), start_time) >= 1500:
                start_recording()
                break
        time.sleep_ms(sample_interval)

def start_recording():
    global sample_freq, umbral, grupo, tiempo, voltaje
    sample_freq = 44100
    sample_interval = 1 / sample_freq
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < 5000:
        lectura = adc.read() * 3.3 / 4095 * 1000000
        tiempo.append(time.ticks_diff(time.ticks_ms(), start_time))
        voltaje.append(lectura)
        time.sleep_ms(sample_interval)
    stop_recording()

def stop_recording():
    global grupo
    save_sd()
    grupo += 1
    tiempo = []
    voltaje = []

def save_sd():
    global grupo, tiempo, voltaje
    try:
        with open('/sd/ruido_grupo_{}.csv'.format(grupo), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Tiempo', 'Voltaje', 'Grupo'])
            for i in range(len(tiempo)):
                writer.writerow([tiempo[i], voltaje[i], grupo])
    except OSError:
        print('Error al montar la tarjeta SD.')

# Bucle infinito
while True:
    escucha()