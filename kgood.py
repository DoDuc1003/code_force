import math
def solution(n):
    if n < 4:
        return -1
    #print(int(math.sqrt(n)) + 1)
    for i in range(3, int(math.sqrt(n)) + 3, 2):
        if (n % i == 0):
            x = n // i
            k = (i + 1) //2
            res = x - k
            if res >= 0:
                return i
    return -1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(solution(n))