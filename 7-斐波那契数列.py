


def fb(x):
    if x<=2:
        return 1
    else:
        return fb(x-1) + fb(x-2)

count = int(input('输入数字:'))

arr = []
for i in range(1,count+1):
    arr.append(fb(i))
print(arr)