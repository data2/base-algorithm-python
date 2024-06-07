


arr = [1,234,3]
print(arr[0])
print(arr[-1])
print(arr[-2])
print(arr[-3])
arr.insert(0,1111)
arr.append(33)
arr.remove(1)
print(arr.index(234))
print(234 in arr)
arr += [23]
print(arr)
print(arr[0:2])
print(arr[::-1])
print(sorted(arr))
print(sorted(arr,reverse=True))
print(max(arr))
print(arr.index(max(arr)))
print(min(arr))
print('============================')
s = 'abcde'
print(s[0])#正向index
print(s[-1])#逆向
print(s[-2])#逆向
print(s[-1*len(s)])#逆向
print(s[0:3])#截取
print(s[::-1])
print('c' in s)