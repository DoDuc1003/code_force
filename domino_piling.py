
def domino(m, n):
    if m == 1:
        return int(n / 2)
    if n == 1:
        return int(m / 2)
    return int(m * n / 2)
if __name__ == '__main__':
    m, n = map(int, input().split())
    print(domino(m, n))