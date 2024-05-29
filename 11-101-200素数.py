

arr = []
for i in range(101,200):
    for j in range(2,i):
        if i%j == 0:
            break
    arr.append(i)

print(arr)