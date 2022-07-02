import math
eps = math.pow(10, - 4)
def arc_cos_angle(edge1, edge2, opposite):
    cos_value = (edge1 * edge1 + edge2 * edge2 - opposite * opposite) / (2 * edge1 * edge2)
    return math.acos(cos_value)


def fmod(a, b):
    if b == 0:
        return -1
    if a == 0:
        return b
    tqout = int(a / b)
    return a - b * tqout

def fgcd(a, b):
    if (b < eps):
        return a

    return fgcd(b, fmod(a, b))
if __name__ == '__main__':
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    x3, y3 = map(float, input().split())

    d1 = math.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
    d2 = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))
    d3 = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

    p = (d1 + d2 + d3) / 2
    s = math.sqrt(p * (p - d1) * (p - d2) * (p - d3))
    r = d1 * d2 * d3 / (4 * s)

    cos_a = arc_cos_angle(edge1=r, edge2=r, opposite=d1)
    cos_b = arc_cos_angle(edge1=r, edge2=r, opposite=d2)
    cos_c = arc_cos_angle(edge1=r, edge2=r, opposite=d3)

    angle = fgcd(cos_a, fgcd(cos_c, cos_b))

    area_of_piece = (r * r * math.sin(angle))/2

    answer = area_of_piece * math.pi * 2 / angle

    print(format(answer, ".8f"))