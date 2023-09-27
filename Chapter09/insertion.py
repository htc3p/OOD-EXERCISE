def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i, -1, -1):
            if temp < arr[j-1] and j > 0:
                arr[j] = arr[j-1]
            else:
                arr[j] = temp
                break
        print(f'Round {i} {arr}')
    return arr
 
 
inp = list(map(int, input("Enter list for number: ").split(",")))
print("Before sort:", inp)
insertionSort(inp)
print("After sort:", inp)