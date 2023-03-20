#!/usr/bin/env python3

from collections import deque

def parse(str, plusprio = 1):
    stack = deque()
    output = []
    ops = { '*':1, '+': plusprio}
    for c in str:
        if c == ' ':
            continue
        if c in ops:
            while len(stack) > 0 and stack[-1] != '(' and ops[c] <= ops[stack[-1]]:
                output.append(stack.pop())
            stack.append(c)
        if c == '(':
            stack.append(c)
        if c == ')':
            while True:
                tmp = stack.pop()
                if tmp == '(':
                    break
                output.append(tmp)
        if c.isdigit():
            output.append(int(c))
    while len(stack) > 0:
        output.append(stack.pop())
    return output

def calc(lst):
    stack = deque()
    for i in lst:
        if i == '*':
            f2 = stack.pop()
            f1 = stack.pop()
            stack.append(f1*f2)
        elif i == '+':
            t2 = stack.pop()
            t1 = stack.pop()
            stack.append(t1+t2)
        else:
            stack.append(i)
    return stack.pop()

def main():
    with open('aoc20_18.txt') as f:
        lines = [ line.strip() for line in f.readlines() ]
    ans1 = 0
    ans2 = 0
    for l in lines:
        ans1 += calc(parse(l, 1))
        ans2 += calc(parse(l, 2))
    print(ans1)
    print(ans2)

if __name__ == '__main__':
    main()
