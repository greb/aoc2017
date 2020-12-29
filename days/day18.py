import collections

class Duet:
    def __init__(self, code):
        self.code = [line.split() for line in code.splitlines()]
        self.pc = 0
        self.regs = dict()
        self.sound = 0
        self.status = 'run'

    def get_val(self, src):
        if src.isalpha():
            return self.regs.get(src, 0)
        return int(src)

    def step(self):
        if self.status == 'halt':
            return

        op, *args = self.code[self.pc]
        ops = {
            'snd': self.op_snd,
            'set': self.op_set,
            'add': self.op_add,
            'mul': self.op_mul,
            'mod': self.op_mod,
            'rcv': self.op_rcv,
            'jgz': self.op_jgz
        }

        ret = ops[op](*args)
        if self.pc >= len(self.code):
            self.status = 'halt'
        return ret

    def op_snd(self, x):
        self.sound = self.get_val(x)
        self.pc += 1

    def op_set(self, x, y):
        self.regs[x] = self.get_val(y)
        self.pc += 1

    def op_add(self, x, y):
        val_x = self.get_val(x)
        val_y = self.get_val(y)
        self.regs[x] = val_x + val_y
        self.pc += 1

    def op_mul(self, x, y):
        val_x = self.get_val(x)
        val_y = self.get_val(y)
        self.regs[x] = val_x * val_y
        self.pc += 1

    def op_mod(self, x, y):
        val_x = self.get_val(x)
        val_y = self.get_val(y)
        self.regs[x] = val_x % val_y
        self.pc += 1

    def op_rcv(self, x):
        val_x = self.get_val(x)
        self.pc += 1
        if val_x != 0:
            return self.sound

    def op_jgz(self, x, y):
        val_x = self.get_val(x)
        val_y = self.get_val(y)

        if val_x > 0:
            self.pc += val_y
        else:
            self.pc += 1


class Duet2(Duet):
    def __init__(self, code, prog_id, rcv, snd):
        super().__init__(code)
        self.rcv = rcv
        self.snd = snd
        self.regs['p'] = prog_id
        self.cnt_snd = 0

    def op_snd(self, x):
        val_x = self.get_val(x)
        self.snd.append(val_x)
        self.cnt_snd += 1
        self.pc += 1

    def op_rcv(self, x):
        if len(self.rcv) > 0:
            self.regs[x] = self.rcv.popleft()
            self.pc += 1
            self.status = 'run'
        else:
            self.status = 'wait'


def part1(inp):
    duet = Duet(inp)

    while duet.status == 'run':
        ret = duet.step()
        if ret is not None:
            break
    return ret


def part2(inp):
    q0 = collections.deque()
    q1 = collections.deque()

    duet0 = Duet2(inp, 0, q0, q1)
    duet1 = Duet2(inp, 1, q1, q0)
    while duet0.status == 'run' or duet1.status == 'run':
        duet0.step()
        duet1.step()

    return duet1.cnt_snd
