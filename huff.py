#!/usr/bin/env/python3
# -*- coding: iso-8859-15 -*-


import huffman
from random import randint
from timer import Timer


def test_basic(numer):
    a = randint(1, 9)
    b = randint(1, 9)
    c = randint(1, 9)
    d = randint(1, 9)
    e = randint(1, 9)
    f = randint(1, 9)
    g = randint(1, 9)
    h = randint(1, 9)
    i = randint(1, 9)
    randy = [('A', a), ('B', b), ('C', c), ('D', d), ('E', e), ('F', f), ('G', g), ('H', h), ('I', i)]
    inpu = []
    for u in range(numer):
        inpu.append(randy[u])
    print(inpu)
    if input() == "":
        output = huffman.codebook(inpu)
        print(output)


if __name__ == "__main__":
    sentinels = ("-")

    while True:
        numy = input("Number of variables..")
        t = Timer()
        test_basic(int(numy))
        input("Press enter when done..")
        print(t.stop())
