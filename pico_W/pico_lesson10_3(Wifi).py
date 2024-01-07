import network
import time

ssid = 'wairan'
password = '29834762'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)

#等待連線失敗
#status=0,1,2正在連線
#status=3連線成功
#<0,>3失敗連線

max_walt = 10
while max_walt > 0:
    status = wlan.status()
    if status < 0 or status >= 3:
        break
    max_walt -= 2
    print("等待連線")
    time.sleep(1)

#檢查目前連線狀態

if wlan.status() != 3:
    raise RuntimeError("連線失敗")
else:
    print('連線成功')
    configure = wlan.ifconfig()
    print(f'IP{configure[0]}')