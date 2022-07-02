
if __name__ == '__main__':
    n, d, m, l = map(int, input().split())
    ans = - 1
    for i in range (0, n):
        value = m * i + l + d
        ans = value - value % d
        if ans < m * (i + 1):
            break
    print(ans)