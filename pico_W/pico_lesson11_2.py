import network
import time
from machine import WDT,ADC,timer #重新開機WDT
#======================================================
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('wairan','29834762')
    #判斷連線是否成功
    #wlan.isconnected() <= bool值 , Ture/False
    #wlan.status() <= bool值
    #status = 0,1,2 正在連線
    #status = 3 連線成功
    #status <= 0 連線失敗 
    #等待最多10s
    Max_unit = 10
    #處理正在連線.....
    while Max_unit > 0:
        Max_unit -= 1
        print("Max_unit:",Max_unit)
        status = wlan.status()
        print("Status:",status)
        if status < 0 or status >= 3:
            break
        print("等待連線")
        time.sleep(1)
    #處理WiFi連線失敗
    if wlan.status() != 3: #!不等於
        #print("連線失敗")
        #產品化一定要重新開機
        #wdt = WDT(timeout=2000) #隔2s
        #wdt.feed() #重新啟動
        raise RuntimeError("連線失敗")
    else:
    #處理WiFi連線成功
        print("連線成功")
        print(wlan.ifconfig())
#======================================================
def alert():
    print('要爆炸了!')
    
def callback1(t:Timer):
    global start
    sensor = ADC(4)    
    vol = sensor.read_u16() * (3.3/65535)
    temperature = 27 - (vol-0.706) / 0.001721
    print(f'溫度:{temperature}')    
    delta = time.ticks_diff(time.ticks_ms(), start)
    print(delta)
    #溫度超過24度,並且發送alert()的時間已經大於60秒
    if temperature >= 24 and delta >= 60 * 1000:        
        alert()
        start = time.ticks_ms()#重新設定計時的時間
        
connect()

start = time.ticks_ms() - 60 * 1000 #應用程式啟動時,計時時間,先減60秒  
time1 = Timer()
time1.init(period=1000,callback=callback1)