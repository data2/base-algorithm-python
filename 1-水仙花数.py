
# 100-1000之间的水仙花数
for i in range(100,1000):
    if ((i//100)**3 + (i//10%10)**3 + (i%10)**3) == i:
        print(i)