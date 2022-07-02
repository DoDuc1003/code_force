
def count_binary(number_max, n):
    if n <= number_max:
        return 1 + count_binary(number_max, 10 * n + 1) + count_binary(number_max, 10 * n)
    else:
        return 0

if __name__ == '__main__':
    n = int(input())
    print(count_binary(n, 1))