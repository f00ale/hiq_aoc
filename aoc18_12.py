#!/usr/local/bin/python3
import re

def solve(data):
    map = {}
    for d in data:
        if m := re.search(r'([\.#]{5}) => ([\.#])', d):
            f = m.group(1)
            t = m.group(2)
            map[f] = t
        elif m := re.search(r'initial state: ([\.#]+)', d):
            plants = m.group(1)

    (offset,iter,pscore,scorediff,diffrepeat) = (0,0,0,0,0)
    while True:
        b = plants.find('#')
        e = plants.rfind('#')

        plants = '....' + plants[b:e+1] + '....'
        offset += b - 4 + 2
        next = ''
        for i in range(len(plants)-4):
            next += map[plants[i:i+5]]

        plants = next

        iter += 1

        score = 0
        for i in range(len(plants)):
            score += i+offset if plants[i] == '#' else 0

        if iter == 20:
            ans1 = score

        if scorediff == score - pscore:
            diffrepeat += 1
        else:
            scorediff = score - pscore
            diffrepeat = 1

        if diffrepeat > 5:
            ans2 = score + scorediff * (50000000000 - iter)
            break

        pscore = score

    print(ans1)
    print(ans2)

def main():
    with open('aoc18_12.txt') as fp:
        data = fp.readlines()
        cleaned = [ line.strip() for line in data ]
        solve(cleaned)

if __name__ == '__main__':
    main()
