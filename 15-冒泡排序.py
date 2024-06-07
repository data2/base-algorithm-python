

arr = [ 5,1,2,8,4]

def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble(arr))
