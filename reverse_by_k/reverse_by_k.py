
test_one = [1]
k = 3


def reverse_by_k(arr, k):
    n = len(arr)
    for i in range(len(arr)//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    print(arr)


reverse_by_k(test_one,k)    

