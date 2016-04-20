import collections
from collections import *

class bunchofstuff:
    def __init__(self):
        self.int = 21
        self.float = 3.3
        self.string = "words"
        self.list = [2, 3, 4, 4, 5, 6]


def MinNumFinder(*argv):
    minnum = 100000
    for arg in argv:
        if type(arg) is int:
            if arg < minnum:
                minnum = arg
        elif type(arg) is float:
            if arg < minnum:
                minnum = arg
        elif type(arg) is str:
            continue
        else:
            for num in arg:
                if num < minnum:
                    minnum = num
    print (minnum)
    return (minnum)

'''
testnum1 = [45]
testnum2 = "butt"
testnum3 = 11
testnum4 = .5
testnum5 = [21321]
testnums1 = [42, 455, 1, 4333, 43434, 111]

MinNumFinder(testnums1, testnum2, testnum3, testnum4, testnum5, testnum1)
'''
