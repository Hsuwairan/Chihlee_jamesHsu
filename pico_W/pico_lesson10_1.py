from machine import ADC,Timer
import time
# Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
#-----------------------------------------------
def alert():
    print("警告")
#-----------------------------------------------
def callback1(t:Timer):
    global start
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(temperature)
    delta = time.ticks_diff(time.ticks_ms(),start)
    print(delta)
#-----------------------------------------------
#判斷溫度警報
    if temperature >=23.5 and delta >=60 * 1000:
        alert()
        start = time.ticks_ms()
        
start = time.ticks_ms() - 60 * 1000 #global計時器
#-----------------------------------------------    
time1 = Timer()
time1.init(period=1000,callback=callback1)