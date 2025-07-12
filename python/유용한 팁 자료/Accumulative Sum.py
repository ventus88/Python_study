# 누적 합계 방식 (Accumulative Sum)


lst1 = [500,200,100,50,30,20,10]
lst2 = [50, 100, 200, 10]

add = 0
for i in lst1:
    if i in lst2:
       add = add + i
print(add)

##########################################################


lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = [10,20,30,40,50,60,70,80,90,100]
add = 0                                            
conunt = 0                                         

for i in range(len(lst1)):                        
    if i>3 and i<9:                              
        add += lst2[i]                            
        conunt += 1                               

print(add/conunt) 