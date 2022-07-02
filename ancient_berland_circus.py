import math

def min_area(d1, d2, d3):
    p = (d1 + d2 + d3)/2;
    s = math.sqrt(p * (p - d1) * (p - d2) * (p - d3))
    return s

if __name__ == '__main__':
    a1, a2 = map(float, input().split())
    b1, b2 = map(float, input().split())
    c1, c2 = map(float, input().split())

    d1 = math.sqrt((b1 - c1) * (b1 - c1) + (b2 - c2) * (b2 - c2))
    d2 = math.sqrt((c1 - a1) * (c1 - a1) + (c2 - a2) * (c2 - a2))
    d3 = math.sqrt((a1 - b1) * (a1 - b1) + (a2 - b2) * (a2 - b2))

    print(d1, d2, d3)
    print(min_area(d1, d2, d3))

