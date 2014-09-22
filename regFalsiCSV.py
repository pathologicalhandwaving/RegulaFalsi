#! /usr/bin/env python

#   regulaFalsiCSV.py

import math

def f(x):
    return math.cos(x) - x**3

def root(a, b):
    return b - (f(b)*((a-b)/(f(a)-f(b))))

def regF(a, b):
    itr = 0
    maxItr = 100
    with open('rfValues.csv', 'w') as f:
        f.write('#itration, f(a), f(b), currentRoot\n')

        while (itr < maxItr):
            r = root(a,b)
            if (r < 0):
                b = r
            else:
                a = r
            f.write('str(itr)'+','+'str(f(a))'+','+'str((f(b)))' + ',' + 'str(r)' + '\n')
            itr = itr + 1
    return r

rootVal = regF(0,1)
print "Value of root is: " + str(rootVal)
