import random

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
if __name__ == '__main__':
    for i in range(10000):
        arr = []
        for _ in range(100):
            arr.append(random.randint(0, 1000))
        random.shuffle(arr)
        selection_sort(arr)
        print(i)
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                raise ValueError("Error")