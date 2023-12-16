from machine import Pin
from machine import Timer

def mycallback1(t):
    print(1)
def mycallback2(t):
    print(2)    
time1 = Timer()
time1.init(freq=1,period=1000,callback=mycallback1)
time2 = Timer()
time2.init(freq=1,period=2000,callback=mycallback2)