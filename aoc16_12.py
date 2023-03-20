#!/usr/bin/env python3

def solve(lst):
    cmds = [tuple(s.split(' ')) for s in lst]
    for p in [0, 1]:
        idx = 0
        regs = {'a': 0, 'b': 0, 'c': p, 'd': 0}
        while idx < len(cmds):
            (c,a,b) = cmds[idx] if len(cmds[idx]) == 3 else cmds[idx] + (None,)
            idx += 1
            if c == 'cpy':
                if a in regs:
                    regs[b] = regs[a]
                else:
                    regs[b] = int(a)
            elif c == 'inc':
                regs[a] += 1
            elif c == 'dec':
                regs[a] -= 1
            elif c == 'jnz':
                if a in regs:
                    if regs[a] != 0:
                        idx += int(b) - 1
                elif int(a) != 0:
                    idx += int(b) - 1
            else:
                print(f'Unknown command {c}')
        print(regs['a'])


def linestolist(str):
    return [x.strip() for x in str.split('\n') if x.strip() != '']

def main():
    solve(linestolist("""
    cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 14 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5
    """))

if __name__ == '__main__':
    main()
