
if __name__ == '__main__':
    n, m, s = map(int, input().split())
    r = (int((m - 1) / s) + 1) * ((m - 1) % s + 1)
    c = (int((n - 1) / s) + 1) * ((n - 1) % s + 1)
    answer = int(r * c)
    print(answer)