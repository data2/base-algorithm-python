
arr = []
for i in range(1,5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i!=j) and j!=k and k!=i and not (100*i + 10*j + k ) in arr :
                arr.append(100*i + 10*j + k )
print(len(arr),arr)