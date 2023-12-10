import random #亂數內建
import pyinputplus as pyip
while(True):
    min = 1
    max = 5
    count = 0
    randomnum = random.randint(min,max)
    print(randomnum)
    while True:
        keyin = pyip.inputInt(f"猜數字範圍{min}~{max}:",min=min,max=max)
        print(keyin)
        if keyin == randomnum:
            print("猜對")
            break
        elif keyin > randomnum:
            print("在小點")
            max = keyin - 1
        elif keyin < randomnum:
            print("在大點")
            min = keyin + 1
        print(f"猜{count}")
pyip.inputYesNo("你還要繼續玩嗎?(y,n)")
if is_play == "no":
    break
print("Game Over")