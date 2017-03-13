#!/usr/bin/env/python3
# -*- coding: iso-8859-15 -*-


def resolve(code, prob):
    prob = {v: k for k, v in prob.items()}
    part = ""
    full = ""
    for char in code:
        part += char
        if part in prob.keys():
            full += prob[part]
            part = ""
    print(full)


prob = {'C': '10', 'A': '0', 'B': '11'}
code = "01110"

resolve(code, prob)
