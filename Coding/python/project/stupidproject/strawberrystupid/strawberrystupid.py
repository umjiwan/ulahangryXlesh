import time
import random
import sys

#딸기가 멍청한지 묻는 코드

#함수


def stupid(): #딸기가 멍청한지 물어보는 함수
    
    # 랜덤으로 문구 출력

    text = random.randint(1, 5)
    
    print("")

    if text == 1: 
        print("딸기는 멍청하지 그렇지?")
    
    elif text == 2:
        print("딸기는 진짜 멍청해")
    
    elif text == 3:
        print("지극히 개인적으로 딸기가 멍청하다고 생각하십니까?")
    
    elif text == 4:
        print("딸기가 멍청하다는 반박측 의견에 동의 하십니까?")
    
    elif text == 5:
        print("딸기는 249 * 9 도 1초만에 못하는 멍청이 입니다 맞습니까? (컴퓨터는 0.0005 초만에 계산 가능)")
    
    else: #논리상 나올 수 없는 값 만약 출력된다면 정말로 치명적인 오류
        print("치명적 오류 errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror")
    
    
    time.sleep(1) # 1초 기다리기

    print("")
    print("-----------------------------")
    print("1. Yes")
    print("2. No")
    print("-----------------------------")
    print("")

    time.sleep(1)
    choice = int(input("숫자만 입력하여 주세요 : ")) # 인풋으로 str을 받고 그걸 int로 변환
    print("")
    time.sleep(2)

    if choice == 1:
        print("정답입니다 당신은 꽤나 지식이 높으신 편이군요")
        time.sleep(1)
        print("프로그램을 종료하겠습니다.")
        time.sleep(2)
        sys.exit()
    
    elif choice == 2:
        print("? 멍청한건 당신도 포함이군요")
        time.sleep(1)
        print("다른 답변을 작성하시길 바랍니다.")
        time.sleep(3)
        stupid1()

def stupid1(): # 동시에 돌아가는 걸 막기위한 함수
    stupid()
    

print("start")
time.sleep(2)
stupid()

