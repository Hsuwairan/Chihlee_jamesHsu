import network
import time
from machine import WDT #重新開機
#======================================================
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