# -*- coding: utf-8 -*-

from myhdl import *
from ula_modules import *

pytestmark = pytest.mark.telemetry("23a-bits", "lab-6", "hw")


def test_halfAdder():
    @instance
    def stimulus():
        for i in range(4):
            t = bin(i, 2)
            a.next = bool(int(t[0]))
            b.next = bool(int(t[1]))
            yield delay(1)
            # print("{} {} {} {}".format(a, b, soma, vaiUm))
            assert soma == (a ^ b)
            assert vaiUm == (a and b)

    a = Signal(bool(0))
    b = Signal(bool(0))
    soma = Signal(bool(0))
    vaiUm = Signal(bool(0))
    dut = halfAdder(a, b, soma, vaiUm)
    sim = Simulation(dut, stimulus)
    sim.run()


def test_fullAdder():
    @instance
    def stimulus():
        for i in range(2**3):
            t = bin(i, 3)
            a.next = bool(int(t[0]))
            b.next = bool(int(t[1]))
            c.next = bool(int(t[2]))
            yield delay(1)
            assert soma == a ^ b ^ c
            assert vaiUm == (a and b) or (a and c) or (c and b)

    a = Signal(bool(0))
    b = Signal(bool(0))
    c = Signal(bool(0))
    soma = Signal(bool(0))
    vaiUm = Signal(bool(0))
    dut = fullAdder(a, b, c, soma, vaiUm)
    sim = Simulation(dut, stimulus)
    sim.run()


def test_adder2bits():
    @instance
    def stimulus():
        for i in range(4):
            x.next = i
            for j in range(4):
                y.next = j
                yield delay(1)
                assert int(s.val) == int(bin(x + y, 2)[-2:], 2)
                print(carry)
                if x + y > 3:
                    assert int(carry) == 1
                else:
                    assert int(carry) == 0

    x = Signal(intbv()[2:])
    y = Signal(intbv()[2:])
    x_ = [x(i) for i in range(2)]
    y_ = [y(i) for i in range(2)]
    s_ = [Signal(bool()) for i in range(2)]
    s = ConcatSignal(*reversed(s_))
    carry = Signal(bool(0))

    dut = adder2bits(x_, y_, s_, carry)
    sim = Simulation(dut, stimulus)
    traceSignals(dut)
    sim.run()


def test_adder():
    @instance
    def stimulus():
        for i in range(64):
            x.next = i
            for j in range(64):
                y.next = j

                yield delay(1)
                assert int(s.val) == int(bin(x + y, 8)[-7:], 2)
                print(carry)
                if x + y > 255:
                    assert int(carry) == 1
                else:
                    assert int(carry) == 0

    x = Signal(intbv()[8:])
    y = Signal(intbv()[8:])
    x_ = [x(i) for i in range(8)]
    y_ = [y(i) for i in range(8)]
    s_ = [Signal(bool()) for i in range(8)]
    s = ConcatSignal(*reversed(s_))
    carry = Signal(bool(0))

    dut = adder(x_, y_, s_, carry)
    sim = Simulation(dut, stimulus)
    sim.run()


def test_bin2bcd():
    @instance
    def stimulus():
        print(h)
        print(m)
        print(l)
        yield delay(10)
        din.next = 13
        yield delay(10)
        print(h)
        print(m)
        print(l)

    din = Signal(intbv(7)[8:])
    h = Signal(intbv(0)[4:])
    m = Signal(intbv(0)[4:])
    l = Signal(intbv(0)[4:])
    dut = bin2bcd(h, m, l, din)
    traceSignals(dut)
    sim = Simulation(dut, stimulus)
    sim.run()
