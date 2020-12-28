import re
import operator

cmp_op_lut = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt
}

def parse(inp):
    instrs = []
    for line in inp.splitlines():
        instrs.append(line.split())
    return instrs


def step(instr, regs):
    reg, op, val, _, cmp_reg, cmp_op, cmp_val = instr

    cmp_reg_val = regs.get(cmp_reg, 0)
    if not cmp_op_lut[cmp_op](cmp_reg_val, int(cmp_val)):
        return

    src_val = regs.get(reg, 0)
    if op == 'inc':
        regs[reg] = src_val + int(val)
    else:
        regs[reg] = src_val - int(val)


def part1(inp):
    instrs = parse(inp)
    regs = {}
    for instr in instrs:
        step(instr, regs)
    return max(regs.values())

def part2(inp):
    instrs = parse(inp)

    max_val = 0
    regs = {}
    for instr in instrs:
        step(instr, regs)
        val = max(regs.values())
        if val > max_val:
            max_val = val
    return max_val
