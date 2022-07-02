
def convert_to_alpha(input):
    res = ""
    input = int(input)
    while (input > 0):
        letter = 'Z'
        c = int(input % 26)
        if c > 0:
            letter = chr(ord('A') + c - 1)
        else:
            input -= 26
        input = int(input / 26)
        res = letter + res

    return res


def convert_to_numeric(row_string):
    res = 0
    for c in row_string:
        res = res * 26 + ord(c) - ord('A') + 1
    return res
if __name__ == '__main__':
    n = int(input())
    for i in range (0, n):
        s = input()
        coordinate = False
        if s[0] == 'R' and '0' <= s[1] and s[1] <= '9' and 1 < s.find('C') and s.find('C') < len(s):
            coordinate = True
        if coordinate:
            c_pos = s.find('C')
            row_str = s[1 : c_pos]
            col_str = s[c_pos + 1 : ]
            col = int(col_str)
            print(convert_to_alpha(col) + row_str)
        else:
            row_str = ""
            col_str = ""
            for char in range (len(s)):
                if (ord(s[char]) >= ord('0') and ord(s[char]) <= ord('9')):
                    col_str = col_str + s[char : ]
                    break
                else:
                    row_str = row_str + s[char]
            print('R' + col_str + 'C' + str(convert_to_numeric(row_str)))