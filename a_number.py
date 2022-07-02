
def sum_base(n, base):
    count = 0
    number = n
    while number > 0:
        x = number % base
        count += x
        number = int(number / base)
    return count

def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    return gcd(b, a % b)
if __name__ == '__main__':
    n = int(input())
    sum = 0
    for i in range(2, n):
        sum += sum_base(n, i)

    numerator = int(sum / gcd(sum, n - 2))
    demonirator = int((n - 2) / gcd(sum, n - 2))
    print(str(numerator) + '/' + str(demonirator))