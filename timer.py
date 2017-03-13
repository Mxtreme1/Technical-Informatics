#!/usr/bin/env/python3
# -*- coding: iso-8859-15 -*-


import datetime


class Timer(object):

    def __init__(self, filename=None):
        self.start_time = datetime.datetime.now()

    def stop(self):
        return datetime.datetime.now() - self.start_time





"""
def time_exercise(fun):

    def time_fun(*args, **kwargs):
        import datetime

        retval = fun(*args, **kwargs)

        while not retval:
            pass
        input("Press enter to finish..")

        run_time = datetime.datetime.now() - start_time

        return run_time

    return time_fun
"""
