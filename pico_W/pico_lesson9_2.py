from machine import Pin
from machine import Timer

def mycallback1(t):
    print(type(t))
time1 = Timer()
time1.init(freq=1,callback=mycallback1)
