

arr = []
for i in range(101,200):
    t= True
    for j in range(2,i):
        if i%j == 0:
            t = False
            break
    if t:
        arr.append(i)

print(arr)