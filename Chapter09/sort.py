# Bubble Sort -----------------------------------------
def bubble_sort(arr):
    for i in range(len(arr)-1, 0,-1):
        swaped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaped = True
        if not swaped:
            break
    return arr

# Selection Sort --------------------------------------
def selection_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        max_pos = 0
        for j in range(1, i+1):
            if arr[j] > arr[max_pos]:
                max_pos = j
        arr[i], arr[max_pos] = arr[max_pos], arr[i]
    return arr

# Heap Sort -------------------------------------------
def fix_down(arr, pos, size):
    temp = arr[pos]
    while 2 * pos + 1 < size:
        child = 2 * pos + 1
        if child + 1 < size and arr[child] < arr[child + 1]:
            child += 1
        if temp >= arr[child]:
            break
        arr[pos] = arr[child]
        pos = child
    arr[pos] = temp

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        fix_down(arr, i, n)  # Fix the heap for the remaining elements

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the root (max) element with the last element
        fix_down(arr, 0, i)  # Fix the heap for the remaining elements

    return arr

# Insertion Sort --------------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i, -1, -1):
            if temp < arr[j-1] and j > 0:
                arr[j] = arr[j-1]
                # print(temp, arr[j])
            else:
                arr[j] = temp
                break
    return arr

# Shell Sort ------------------------------------------
def shell_sort(arr):
    dIncrements = [109, 41, 19, 5, 1]   # define incremental sequence
    for d in dIncrements:
        for i in range(d, len(arr)):
            temp = arr[i]
            for j in range(i, -1, -d):
                if temp < arr[j-d] and j >= d:
                    arr[j] = arr[j-d]
                else:
                    arr[j] = temp
                    break
    return arr

# Merge Sort ------------------------------------------
def merge(arr, start, mid, end):
    temp = []
    bi = start      # index of B
    ci = mid + 1    # index of C
    
    for i in range(start, end+1):
        if ci > end:
            temp.append(arr[bi])
            bi += 1
            continue
        if bi > mid:
            temp.append(arr[ci])
            ci += 1
            continue
        
        if arr[bi] < arr[ci]:
            temp.append(arr[bi])
            bi += 1
        else:
            temp.append(arr[ci])
            ci += 1

    for i in range(start, end+1):
        arr[i] = temp[i - start]  # Adjust the index to match the temporary list
        
def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)
    return arr
    
# Quick Sort ------------------------------------------
def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while left < right:
        if arr[left] <= pivot:
            left += 1
        elif arr[right] > pivot:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    if arr[left] > pivot:
        left -= 1
    arr[start], arr[left] = arr[left], arr[start]
    return left

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        print(pivot)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr



if __name__ == '__main__':
    l1 = [18, 2, 4, 5, 3, -2]
    l2 = [8, 6, 7, 5, 9]
    # print(merge_sort(l1, 0, len(l1)-1))
    print(quick_sort(l2, 0, len(l2)-1))