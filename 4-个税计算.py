
a = [100000,100000,200000,200000,400000]
b = [0.1,0.075,0.05,0.03,0.015,0.01]

x = int(input('请输入数值:'))
s = 0
for i in range(5):
    if x < a[i]:
        s += x*b[i]
        x = 0
        break
    else:
        s += a[i]*b[i]
        x -= a[i]

s += x * b[-1]

print(s)

