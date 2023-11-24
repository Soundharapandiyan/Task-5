# 2. Create of pyramid of numbers from 1 to 20.
num = 1 
for i in range(1,7) : 
    for j in range(1,i+1) :
        if num <=20:
            print(num , end=" ")
            num += 1
    print()