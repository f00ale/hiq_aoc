#!/usr/bin/env python3
import re

def calcA(str):
    class n:
        def __init__(self,v):
            self.val = v
        def __add__(self, other):
            return n(self.val + other.val)
        def __sub__(self, other):
            return n(self.val * other.val)
    str = str.replace('*','-')
    str = re.sub(r'([0-9]+)', r'n(\1)', str)
    return eval(str).val

def calcB(str):
    class n:
        def __init__(self,v):
            self.val = v
        def __add__(self, other):
            return n(self.val * other.val)
        def __mul__(self, other):
            return n(self.val + other.val)
    str = str.replace('*','-')
    str = str.replace('+', '*')
    str = str.replace('-', '+')
    str = re.sub(r'([0-9]+)', r'n(\1)', str)
    return eval(str).val


def main():
    with open('aoc20_18.txt') as f:
        lines = [ line.strip() for line in f.readlines() ]
    ans1 = 0
    ans2 = 0
    for l in lines:
        ans1 += calcA(l)
        ans2 += calcB(l)
    print(ans1)
    print(ans2)
if __name__ == '__main__':
    main()
