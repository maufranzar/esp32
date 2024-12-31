# Proyecto IoT con ESP32-C3, LoRa y Sensores

¡Bienvenido(a) a este repositorio! Aquí encontrarás el código y la documentación necesaria para el despliegue de un sistema IoT que integra ESP32 (y variantes como el ESP32-C3), conexiones LoRa y diversos sensores para recopilar datos de manera remota. También se incluye una configuración de backend con Docker, MongoDB y servicios para la persistencia de datos.

---

## Tabla de Contenidos
- [Proyecto IoT con ESP32-C3, LoRa y Sensores](#proyecto-iot-con-esp32-c3-lora-y-sensores)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción General](#descripción-general)
  - [Estructura del Proyecto](#estructura-del-proyecto)

---

## Descripción General

Este proyecto se compone de varios módulos:
- **Firmware ESP32/ESP32-C3**: Permite la lectura de sensores y la transmisión de datos.
- **LoRa**: Scripts y librerías para establecer comunicación LoRa entre nodos (Tx/Rx).
- **Backend**: Contiene la configuración de contenedores Docker, una aplicación FastAPI y una base de datos MongoDB para almacenar y procesar los datos recopilados.
- **Documentación (docs)**: Incluye tanto fichas técnicas de los módulos de hardware (datasheet) como binarios de firmware precompilados.

El objetivo principal es proporcionar una arquitectura escalable y modular para proyectos de IoT que involucren adquisición de datos, transmisión inalámbrica y persistencia en una base de datos.

---

## Estructura del Proyecto

La estructura de directorios es la siguiente:

```bash
.
├── backend
│   ├── app
│   │   └── main.py            # Código principal de la aplicación FastAPI
│   ├── docker-compose.yml      # Configuración de servicios para Docker
│   ├── Dockerfile              # Dockerfile para construir la imagen
│   └── mongo-init
│       ├── mongod.conf         # Configuración de MongoDB
│       ├── start.sh            # Script de inicio para MongoDB
│       └── validation.js       # Scripts de validación / inicialización de la BD
├── docs
│   ├── datasheet               # Fichas técnicas de hardware
│   │   ├── AJ-SR04M.pdf
│   │   ├── DHT_11.pdf
│   │   ├── esp32-c3_datasheet_en.pdf
│   │   ├── esp32-c3-mini-1_datasheet_en.pdf
│   │   ├── esp32_datasheet_en.pdf
│   │   ├── GY-302-BH1750.pdf
│   │   ├── isa-summary.pdf
│   │   ├── MAX4465-MAX4469.pdf
│   │   ├── RFM95_96_97_98W.pdf
│   │   ├── SCT-013-30A.pdf
│   │   └── SDCard_Adapter.pdf
│   └── firmware                # Binarios precompilados de MicroPython
│       ├── ESP32_GENERIC-20240222-v1.22.2.bin
│       └── ESP32_GENERIC_C3-20240222-v1.22.2.bin
├── LICENSE                     # Licencia del proyecto
├── LoRa
│   ├── lib                     # Librerías de comunicación LoRa
│   │   ├── async_modem.py
│   │   ├── __init__.py
│   │   ├── lora_rd_settings.py
│   │   ├── modem.py
│   │   └── sx127x.py
│   ├── Rx                      # Ejemplo de código para receptor LoRa
│   │   ├── boot.py
│   │   └── main.py
│   └── Tx                      # Ejemplo de código para transmisor LoRa
│       ├── boot.py
│       └── main.py
├── README.md                   # Este archivo
├── sensors
│   ├── boot.py
│   ├── check.py
│   ├── lcd_i2c                 # Librería para manejar displays LCD por I2C
│   │   ├── const.py
│   │   ├── __init__.py
│   │   ├── lcd_i2c.py
│   │   ├── typing.py
│   │   └── version.py
│   ├── main.py                 # Código principal para lectura de sensores
│   ├── record.py               # Registro y guardado de datos
│   ├── sdcard.py               # Manejo de tarjeta SD
│   ├── sensor.py               # Módulo para inicializar y leer sensores
│   └── variables.py            # Configuraciones globales de sensores
├── sound
│   ├── boot.py
│   ├── constants.py
│   ├── lcd_i2c                 # Librería LCD I2C enfocada en el módulo de sonido
│   │   ├── const.py
│   │   ├── __init__.py
│   │   ├── lcd_i2c.py
│   │   ├── typing.py
│   │   └── version.py
│   ├── main.py                 # Código para captura/procesamiento de sonido
│   └── sdcard.py               # Manejo de tarjeta SD para datos de audio
└── TL
    ├── boot.py
    ├── eco.txt                 # Archivo de configuración o datos específicos
    └── main.py
