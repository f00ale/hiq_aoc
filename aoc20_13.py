#!/usr/bin/env python3

def solve(start, data):
    min = 10e100
    for d in data:
        if d != 'x':
            n = int(d)
            tmp = n - start % n
            if tmp < min:
                min = tmp
                ans1 = min * n

    print(ans1)

    def inv(a, m):
        m0 = m
        x0 = 0
        x1 = 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            t = m
            m = a % m
            a = t
            t = x0
            x0 = x1 - q * x0
            x1 = t
        if x1 < 0:
            x1 += m0
        return x1

    co = []
    for i in range(len(data)):
        if data[i] != 'x':
            n = int(data[i])
            co.append(((n-i)%n,n))

    M = 1
    for a,m in co:
        #print(f'{a} {m}')
        M *= m


    ans2 = 0
    for a,m in co:
        b = M // m
        ans2 += a * b * inv(b, m)

    ans2 = ans2 % M

    print(ans2)

def main():
    with open('aoc20_13.txt') as f:
        l = f.readlines()
        start = int(l[0])
        data = l[1].split(',')
        solve(start, data)


if __name__ == '__main__':
    main()
