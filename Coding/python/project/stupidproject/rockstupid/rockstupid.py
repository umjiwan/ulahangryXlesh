import sys
import time

#함수

def rockstupid():
    time.sleep(1)
    print("맞아 넌 천재구나!")
    time.sleep(3)

def rocksmart():
    time.sleep(1)
    print("그럴리가 오히려 너가 멍청이구나")
    time.sleep(3)
    sys.exit(1)

def start():
    time.sleep(1)
    print("안녕! 원민이는 멍청하니?")
    choice()

def choice():
    time.sleep(1)
    print("")
    print("1. Yes")
    print("2. No")
    print("")
    time.sleep(1)
    choice_nu = int(input("숫자만 입력해줘 : "))
    print("")
    if choice_nu == 1:
        rockstupid()   
    elif choice_nu == 2:
        rocksmart()    
    else:
        print("Error 숫자만 입력해")
start()


