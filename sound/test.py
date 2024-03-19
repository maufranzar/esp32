import numpy as np
import sounddevice as sd

# Generar un tono de 440 Hz
fs = 44100  # Frecuencia de muestreo
f = 440  # Frecuencia del tono
x = np.linspace(0, 10, 10*fs, False)  # Array de tiempo de 10 segundos
y = np.sin(f * 2 * np.pi * x)  # Generar el tono

# Reproducir el tono
sd.play(y, fs)