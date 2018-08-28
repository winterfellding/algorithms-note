import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        tmp = arr[i]
        while tmp < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp

if __name__ == '__main__':
    for i in range(10000):
        arr = []
        for _ in range(100):
            arr.append(random.randint(0, 1000))
        random.shuffle(arr)
        insertion_sort(arr)
        print(i)
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                raise ValueError("Error")
         
                