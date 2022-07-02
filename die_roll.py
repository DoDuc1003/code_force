
def gcd(a, b):
    if a == 0 or b == 0:
        return a + b

    return gcd(b, a % b)
if __name__ == '__main__':
    x, y = map(int, input().split())
    m = max(x, y)
    numerator = 6 - m + 1
    denominator = 6
    g = gcd(numerator, denominator)

    numerator = int(numerator / g)
    denominator = int(denominator / g)

    print(str(numerator) + '/' + str(denominator))
