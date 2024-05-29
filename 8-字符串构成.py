


str = input('请输入一串字符串:')

alpha = 0
space = 0
digit = 0
others = 0
for i in range(len(str)):
    if str[i].isalpha():
        alpha += 1
    elif str[i].isspace():
        space += 1
    elif str[i].isdigit():
        digit += 1
    else:
        others += 1
print(alpha,space,digit,others)

