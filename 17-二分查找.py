

def binary_search(arr,target):
    left,right = 0,len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] >target :
            right = mid - 1
        else:
            left = mid + 1

    return -1

print(binary_search([1,2,4,5,7,10],5))
#必须先排序
# sorted(arr)
# print(binary_search(sorted([11,2,42,5,7,10]),5))