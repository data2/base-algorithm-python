


month = int(input('请输入月数:'))
m1 = 1
m2 = 0
m3 = 0
old = 0
for n in range(month-1):
    old = old + m3
    m3 = m2
    m2 = m1
    m1 = m3 + old

print(m1+m2+m3+old)
