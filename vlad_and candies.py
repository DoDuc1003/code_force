

def solve(candies):
    if len(candies) == 1:
        if (candies[0] > 1):
            return False
        else:
            return True

    candies.sort(reverse=True)
    if candies[0] - candies[1] <= 1:
        return True
    return False

if __name__ == '__main__':
    test = int(input())
    for test_case in range (test):
        n = int(input())
        candies = []
        candies = [int(x) for x in input().split()]
        if (solve(candies)):
            print("YES")
        else:
            print("NO")