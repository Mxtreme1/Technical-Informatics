#!/usr/bin/env/python3
# -*- coding: iso-8859-15 -*-


from random import randint
from timer import Timer
import webbrowser


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

prime_implicants(6)
