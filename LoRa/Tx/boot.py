# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import webrepl
import network

# WIFI Init
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect('MAU','Hakanamatata00,')

