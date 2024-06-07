



arr = [ 5,1,2,8,4]

def select(arr):
    for i in range(len(arr)):
        t = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[t] :
                t= j
        arr[i],arr[t] = arr[t],arr[i]
    return arr

print(select(arr))
