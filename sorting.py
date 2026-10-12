# bubble sort 
data = [24, 22, 44, 66, 88, 72, 2, 4]
n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print("sorted array is:", data)
