rum = int(input("숫자를 입력하세요"))

if rum>=100000 and rum<1000000:
    moreT = rum//1000
    lessT = rum%1000
    print(moreT,",",lessT)
    print(str(moreT)+","+str(lessT))
    print("%d,%d" %(moreT,lessT))
    print(f"{moreT},{lessT}")