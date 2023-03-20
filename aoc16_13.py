#!/usr/bin/env python3

from collections import deque

def solve(inp):
    def popcnt(num:int):
        return num.bit_count()

    def tile(x,y,input):
        return '#' if popcnt(x*x + 3*x + 2*x*y + y + y*y + input) % 2 == 1 else ' '

    target = (31,39)
    q = deque()
    q.append((0,1,1))
    visited = set()
    while q:
        (s,x,y) = q.popleft()
        if (x,y) in visited:
            continue
        if tile(x,y,inp) == '#':
            continue
        if (x,y) == target:
            ans1 = s
            break
        visited.add((x,y))
        if x > 0:
            q.append((s+1,x-1,y))
        if y > 0:
            q.append((s+1,x,y-1))
        q.append((s+1,x+1,y))
        q.append((s+1,x,y+1))

    print(ans1)

    q.clear()
    q.append((0,1,1))
    visited = set()
    while q:
        (s,x,y) = q.popleft()
        if s > 50:
            continue
        if tile(x,y,inp) == '#':
            continue
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if x > 0:
            q.append((s+1,x-1,y))
        if y > 0:
            q.append((s+1,x,y-1))
        q.append((s+1,x+1,y))
        q.append((s+1,x,y+1))

    ans2 = len(visited)
    print(ans2)

def main():
    solve(1362)


if __name__ == '__main__':
    main()
