#!/usr/bin/env python3
from collections import deque
import heapq

def makedata2(data):
    def add1(l, a):
        r = ''
        for d in l:
            n = int(d)+a
            if n > 9:
                n -= 9
            r += chr(ord('0')+n)
        return r
    ret = []
    for row in range(5):
        for l in data:
            line = ''
            for col in range(5):
                line += add1(l,row+col)
            ret.append(line)
    return ret

def solve(data):
    scores = []
    MAXY = len(data)
    MAXX = len(data[0])
    for r in range(MAXY):
        scores.append( MAXX * [ 2**16 ])

    scores[0][0] = 0
    q = [(0,0,0)]
    while q:
        (s,x,y) = heapq.heappop(q)
        if s > scores[y][x]:
            continue
        for (dx,dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny = y + dy
            if ny < 0 or ny >= MAXY:
                continue
            nx = x + dx
            if nx < 0 or nx >= MAXX:
                continue
            if s + int(data[ny][nx]) < scores[ny][nx]:
                scores[ny][nx] = s + int(data[ny][nx])
                heapq.heappush(q, (scores[ny][nx],nx,ny))

    return scores[-1][-1]

def main():
    with open('aoc21_15.txt') as fp:
        lines = [ line.strip() for line in fp.readlines() ]

    ans1 = solve(lines)
    print(ans1)

    ans2 = solve(makedata2(lines))
    print(ans2)


if __name__ == '__main__':
    main()
