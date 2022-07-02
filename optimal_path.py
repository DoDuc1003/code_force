
def sum_of_path_optimal(n, m):
    if m == 1:
        return n * (n + 1) / 2
    if n == 1:
        return m * (m + 1) / 2

    right_down = m * (m + 1) / 2 + m * n + (n - 1) * n / 2 * m - m
    down_right = n + (n - 1) * m * m + m + (n - 1) * n / 2 * m - (n - 1) * m - 1
    if (right_down > down_right):
        return down_right
    return right_down
if __name__ == '__main__':
    test = int(input())
    for test_case in range (test):
        n, m = map(int, input().split())
        print(int(sum_of_path_optimal(n, m)))
