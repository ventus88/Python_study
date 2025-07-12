# 자판기 프로그램

import sys

cof = 2
tea = 2

while True:
    ex = input("종료하실려면 0번을 입력해주세요 or 계속 하실려면 아무키나 적으세요")
    if ex == "0":
        sys.exit()
    
    menu = input("커피/녹차 를 골라 주세요").strip()

    
    while True:
        try:
            cash = int(input("커피는 300원,녹차는 200원 입니다"))
            break
        except ValueError:
            print("숫자만 입력해주세요")
    
    
    if cof ==  0 and tea == 0: 
        print("모든재고가 없습니다")
        break
    if menu == "커피" and cof == 0:
        print("커피 재고가 없습니다")
        continue
    if menu == "녹차" and tea == 0:
        print("녹차 재고가 없습니다")
        continue
    
    
    if menu == "커피":
        if cash == 300:
            cof -= 1
            print("고르신 커피가 나옵니다")
            print(f"현재 재고는 {cof}개 입니다".format(cof))
        elif cash > 300:
            re_turn = cash - 300
            cof -= 1
            print("고르신 커피가 나옵니다")
            print(f"거스름돈은 {re_turn}원 입니다")
            print(f"현재 재고는 {cof}개 입니다".format(cof))
        elif cash < 300:
            print("돈이 부족합니다")
            total_cash = cash
            while True:
                res = 300 - total_cash
                re_cash = int(input("현재 부족한 금액은{}원 입니다 넣어주세요".format(res)))
                total_cash += re_cash
                if total_cash >= 300:
                    cof -= 1
                    print("고르신 커피가 나옵니다")
                    print(f"현재 재고는 {cof}개 입니다".format(cof))
                    break
       
    elif menu == "녹차":
        if cash == 200:
            tea -= 1
            print("고르신 녹차가 나옵니다")
            print(f"현재 재고는 {tea}개 입니다".format(tea))
        elif cash > 200:
            re_turn = cash - 200
            tea -= 1
            print("고르신 녹차가 나옵니다")
            print(f"거스름돈은 {re_turn}원 입니다")
            print(f"현재 재고는 {tea}개 입니다".format(tea))
        elif cash < 200:
            print("돈이 부족합니다")
            total_cash = cash
            while True:
                res = 200 - total_cash
                re_cash = int(input("현재 부족한 금액은{}원 입니다 넣어주세요".format(res)))
                total_cash += re_cash
                if total_cash >= 200:
                    tea -= 1
                    print("고르신 녹차가 나옵니다")
                    print(f"현재 재고는 {tea}개 입니다".format(tea))
                    break
       
    else:
        print("잘못 입력하셨습니다 다시 입력해 주세요")
   