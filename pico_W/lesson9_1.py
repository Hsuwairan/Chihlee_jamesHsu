from machine import Pin
import time

led = Pin("LED",Pin.OUT)
while True: 
    led.on()
    time.sleep_ms(100)
    led.off()
    time.sleep_ms(100)
    led.on()
    time.sleep_ms(100)
    led.off()
    time.sleep_ms(100)
