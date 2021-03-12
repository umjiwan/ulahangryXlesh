import time
import datetime
import sys
import random

def dice():
    time.sleep(1)
    print("")
    print("주사위의 최대 숫자를 입력하여 주세요.")
    time.sleep(0.5)
    Max = int(input("숫자만 입력 : "))
    time.sleep(1)
    print("")
    print("주사위를 굴리는 중 입니다.")
    time.sleep(1)
    dice_nu = random.randint(1, Max)
    print(f"주사위의 숫자는 {dice_nu} 입니다 !")
    
    f = open("dice_log.txt", "a")
    now = datetime.datetime.today()
    f.write(f"\n주사위의 숫자는 {dice_nu} - {now}\n")
    f.close()

    time.sleep(1)
    print("")
    print("주사위를 한번 더 굴리시겠습니까?")
    
    time.sleep(0.5)
    print("")
    print("1. Yes")
    print("2. No")
    print("")
    time.sleep(1)
    more = int(input("숫자만 입력 : "))
    
    if more == 1:
        time.sleep(1)
        onemore()
    elif more == 2:
        time.sleep(1)
        print("")
        print("프로그램을 종료합니다.")
        time.sleep(3)
        sys.exit()
    else: 
        time.sleep(1)
        print("")
        print("Error")
        time.sleep(2)
        sys.exit()

def onemore():
    time.sleep(0.5)
    print("")
    print("주사위를 한번 더 던집니다.")
    dice()

print("hello!")
dice()


