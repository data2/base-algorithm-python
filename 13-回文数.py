

x = input('请输入5位数字：')

# 直接判断
def isHws(x):
    return x[-5] == x[-1] and x[-4] == x[-2]

print(isHws(x))

#与反转比较

print(x==x[::-1])


#双指针

for i in range(len(x)):
    j = len(x) - 1 -i
    if x[i] != x[j]:
        print(False)
        break
print(True)

def isOk(x):
    i=0
    j=len(x)-1
    while i!=j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True
print(isOk(x))