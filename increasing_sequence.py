def count_increase(arr, d):
    count = 0
    for i in range (1, len(arr)):
        if (arr[i-1] >= arr[i]):
            x = int ((arr[i-1] - arr[i]) / d) + 1
            arr[i] = arr[i] + x * d;
            count = count + x
    return count

if __name__ == '__main__':
    n, d = map(int, input().split())
    arr = [int(x) for x in input().split()]
    print(count_increase(arr, d))
