#!/usr/bin/env python3

def solve(str, width, height):
    lines = []
    start = 0
    while start < len(str):
        lines.append(str[start:(start+width*height)])
        start += width*height

    cnts = []

    for l in lines:
        cnts.append(l.count('0'))

    minidx = cnts.index(min(cnts))
    ans1 = lines[minidx].count('1')*lines[minidx].count('2')
    print(ans1)

    ans2 = ''
    for c in range(len(lines[0])):
        for l in range(len(lines)):
            if lines[l][c] == '2':
                continue
            else:
                if lines[l][c] == '0':
                    ans2 += ' '
                else:
                    ans2 += '#'
                break

    start = 0
    while start < len(ans2):
        print(ans2[start:start+width])
        start += width



def main():
    with open('aoc19_08.txt') as fp:
        data = fp.readline().strip()
        solve(data, 25, 6)

if __name__ == '__main__':
    main()
