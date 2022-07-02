import math

if __name__ == '__main__':
    a, b, c = map(int, input().split())

    if a == 0:
        if b == 0:
            if c == 0:
                print("-1")
            else:
                print("0")
        else:
            print("1")
            x = -c/b
            print("{:.10f}".format(x))
    else:
        denta = b * b - 4 * a * c
        if denta == 0:
            x = -b/(2*a)
            print("1")
            print("{:.10f}".format(x))
        else:
            if denta < 0:
                print("0")
            else:
                x1 = (-b - math.sqrt(denta)) / (2 * a)
                x2 = (-b + math.sqrt(denta)) / (2 * a)
                if (x1 > x2):
                    temp = x1
                    x1 = x2
                    x2 = temp
                print("2")
                print("{:.10f}".format(x1))
                print("{:.10f}".format(x2))