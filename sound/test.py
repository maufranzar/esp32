import pyaudio
import numpy as np
import signal
import sys

# Frecuencia del tono
f = 220.0
amplitude = 0.5

# Función para generar la onda sinusoidal
def generate_tone(frequency, amplitude, duration, fs):
    t = np.linspace(0, duration, int(fs * duration), False)
    return amplitude * np.sin(frequency * t * 2 * np.pi)

# Inicializar PyAudio
p = pyaudio.PyAudio()

# Abrir un stream
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True)

# Manejar la interrupción
def signal_handler(signal, frame):
    stream.stop_stream()
    stream.close()
    p.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Generar un tono de 1 segundo
tone = generate_tone(f, amplitude, 5, 44100)

# Reproducir el tono
stream.write(tone.astype(np.float32).tostring())