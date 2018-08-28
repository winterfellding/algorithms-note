import random

def quicksort(arr, low, high):
    if low < high:
        partion_idx = partition(arr, low, high)
        quicksort(arr, low, partion_idx-1)
        quicksort(arr, partion_idx+1, high)

def partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo+1
    j = hi
    while True:
        while True:
            if arr[i] <= pivot and i < hi:
                i += 1
            else:
                break
        while True:
            if arr[j] > pivot and j > lo:
                j -= 1
            else:
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    return j

if __name__ == '__main__':
    for i in range(10000):
        arr = []
        for _ in range(100):
            arr.append(random.randint(0, 1000))
        random.shuffle(arr)
        print(i)
        quicksort(arr, 0, len(arr)-1)
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                raise ValueError("Error")
