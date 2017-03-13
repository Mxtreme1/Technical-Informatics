#!/usr/bin/env/python3
# -*- coding: iso-8859-15 -*-


from random import randint
import huffman
from timer import Timer
from quine_mccluskey.qm import QuineMcCluskey
import os
import time
import webbrowser


qm = QuineMcCluskey()


def test_basic(numer):
    a = randint(0, 9)
    b = randint(0, 9)
    c = randint(0, 9)
    d = randint(0, 9)
    e = randint(0, 9)
    f = randint(0, 9)
    g = randint(0, 9)
    h = randint(0, 9)
    i = randint(0, 9)
    randy = [('A', a), ('B', b), ('C', c), ('D', d), ('E', e), ('F', f), ('G', g), ('H', h), ('I', i)] # noqa E501
    inpu = []
    for u in range(numer):
        inpu.append(randy[u])
    print(inpu)
    if input() == "":
        output = huffman.codebook(inpu)
        print(output)


def mkquine(numb):
    twos = set()
    while len(twos) < numb:
        x = randint(0, 15)
        twos.add(x)
    for n in twos:
        print("{0:04b}".format(n))
    if input() == "":
        print(qm.simplify(list(twos), []))


def prime_implicants(user_input):
    stri = ""
    c = []
    for x in range(user_input):
        c.append(x)
    url = "http://www.quinemccluskey.com/index.php?min="
    stri += str(c[0])
    for i in range(len(c) - 1):
        q = randint(0, 15)
        stri += "%0D%0A" + str(q)
        print("{0:04b}".format(q))
    webbrowser.open(url + stri + "&dont=")


def makemysheet():
    inpu = input("Number of execercises?  ")
    num = int(inpu)
    print("Sheet created!")
    for exer in range(num):
        sentinels = ("-")
        x = randint(0, 3)
        if x == 0:
            print("Have fun with the Huffman Code \n")
            numy = input("Number of variables..")
            t = Timer()
            test_basic(int(numy))
            input("Press enter when done..")
            print(t.stop())
            time.sleep(4)
            os.system('clear')
        elif x == 1:
            print("Do the McCluskey \n")
            user_input = input("Number of variables..")
            if user_input in sentinels:
                break
            t = Timer()
            mkquine(int(user_input))
            input("Press enter when done..")
            print(t.stop())
            time.sleep(4)
            os.system('clear')
        elif x == 2:
            print("Not ROBDDs again \n")
            user_input = input("Number of Variables..")
            if user_input in sentinels:
                break
            t = Timer()
            mkquine(int(user_input))
            input("Press enter when done..")
            print(t.stop())
            time.sleep(4)
            os.system('clear')
        elif x == 3:
            print("A wild Prime Implicant Chart appears \n")
            user_input = input("Number of Variables..")
            if user_input in sentinels:
                break
            t = Timer()
            prime_implicants(int(user_input))
            input("Press enter when done..")
            print(t.stop())
            time.sleep(4)
            os.system('clear')


if __name__ == "__main__":
    os.system("clear")
    sheets = input("How many sheets must a man do ... until he can get an A?  ")
    for sheet in range(int(sheets)):
        os.system("clear")
        makemysheet()
