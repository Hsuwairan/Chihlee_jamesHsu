import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Galaxy S21 Ultra 5G','29834762')

while not wlan.isconnected() and wlan.status() >= 0:
    print("等待連線...")
    time.sleep(1)
    
print(wlan.ifconfig())