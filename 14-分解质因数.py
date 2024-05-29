
#递归算法

def is_zhishu(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


def get_zhishu_arr(x):
    arr = []
    for i in range(2,x):
        if x % i ==0 :
            arr.append(i)
            arr.append(int(x/i))
            print(arr)
            for element in arr:
                if is_zhishu(element):
                    continue
                else:
                    arr.remove(element)
                    add_arr(arr,get_zhishu_arr(element))
            break
    return arr

def add_arr(arr,arr2):
    for x in arr2:
        if x in arr:
            continue
        else:
            arr.append(x)

print(get_zhishu_arr(int(input('请输入一个数字'))))

