

x = int(input('请输入一个不多于5位的正整数:'))

print(len(str(x)))
print(str(x)[::-1])

s = ''
for i in range(len(str(x))-1,-1,-1):
    s += str(x)[i]

print(s)