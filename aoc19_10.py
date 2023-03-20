#!/usr/bin/env python3

from math import gcd
from math import atan2, pi

def solve(data):
    asteroids = []
    for y in range(len(data)):
        start = 0
        while start >= 0:
            x = data[y].find('#',start)
            if(x >= 0):
                #print(f'{x}x{y}')
                asteroids.append((x,y))
                start = x + 1
            else:
                start = x
    ans1 = 0
    bestp = (0,0)

    for p in asteroids:
        deltas = {}
        for o in asteroids:
            if p == o:
                continue
            d = (o[0]-p[0], o[1]-p[1])
            g = gcd(d[0],d[1])
            d = (d[0]//g, d[1]//g)
            deltas[d] = None
        if len(deltas) > ans1:
            ans1 = len(deltas)
            bestp = p

    #print(bestp)
    dirs = {}
    for p in asteroids:
        if p == bestp:
            continue
        dx = bestp[0]-p[0]
        dy = bestp[1]-p[1]
        g = gcd(dx,dy)
        dx = dx / g
        dy = dy / g
        v = atan2(-dx,dy)
        if v < -.00001:
            v += 2 * pi
        if (dx,dy) in dirs:
            dirs[(dx,dy)].append((v,g,p))
        else:
            dirs[(dx,dy)] = [ (v,g,p) ]

    order = [ v for v in dirs.values() ]
    for o in order:
        o.sort(key=lambda x : x[1])
    order.sort(key=lambda x : x[0])

    destroyed = 0
    TOFIND = 200
    for o in order:
        if len(o) > 0:
            destroyed += 1
            if destroyed == TOFIND:
                lastp = o[0][2]
                ans2 = 100 * lastp[0] + lastp[1]
                break


    print(ans1)
    print(ans2)

    print(order[199][0][2])

def main():
    with open('aoc19_10.txt') as file:
        solve( [ line.strip() for line in file.readlines() ] )

if __name__ == '__main__':
    main()
