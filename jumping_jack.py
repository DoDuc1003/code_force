import math
def jumping(n):
    if (n == 0):
        return 0
    answer = 0
    p = 1
    sum = 0
    while sum < n:
        sum = sum + p
        p = p + 1
        answer = answer + 1
    distance = sum - n
    if distance % 2 == 0:
        return answer
    else:
        if (distance + p) % 2 == 0:
            return answer + 1
        else :
            return answer + 2
if __name__ == '__main__':
    n = int(input())
    if n < 0:
        n = -n

    print(jumping(n))