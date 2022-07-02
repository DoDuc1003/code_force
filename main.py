
import array
import math


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
def solve(n, k, a):
    a.sort()
    for i in range(n):
        x = a[i] + k
        pos = binary_search(a, 0, n-1, x)
        if pos != -1:
            return "YES"
    return "NO"

if __name__ == '__main__':
    n = 4
    a = [1, 3, 4, 2]

    for i in range (0, n):
        for j in range (1, n - i + 1):
            for k in range(0, j):
                print(a[i+k], end=" ")
            print()