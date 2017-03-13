#!/usr/bin/env/python3
# -*- coding: iso-8859-15 -*-


from quine_mccluskey.qm import QuineMcCluskey
from random import randint

from timer import Timer

qm = QuineMcCluskey()


def mkquine(numb):
    twos = set()
    while len(twos) < numb:
        x = randint(0, 15)
        twos.add(x)
    for n in twos:
        print("{0:04b}".format(n))
    if input() == "":
        print(qm.simplify(list(twos), []))


if __name__ == "__main__":
    sentinels = ("-")

    while True:
        user_input = input("Number of variables..")
        if user_input in sentinels:
            break
        t = Timer()
        mkquine(int(user_input))
        input("Press enter when done..")
        print(t.stop())
