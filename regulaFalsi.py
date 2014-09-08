#! /usr/bin/env python 

#   Kristi Short
#   Numerical Analysis 
#   Math180
#   Fall 2014
#   Hwk#2: RegulaFalsi with Illinois Modification 

#   Let h(x) = cos(x) - x^3 = 0, for x element of the Reals.
#   Then let f(x) = cos(x) 
#   And g(x) = x^3
#   We want to find where f(x) = g(x).
#   i.e. Where h(x) has a zero. 


import math


#   Vars
itr = itr + 1
a = (-.5)       # x_0
b = 1           # x_1
x = 0
f = math.cos(x)
g = x**3


#   h(x) is an odd function, so it has only one root at x = 0.86547403310161444662

def f(x):
    return math.cos(x) - x**3 
f(a);
f(b);

def see(a,b):
    c = (a*f(b) - b*f(a))/(f(b) - f(a))
    return c

see(a, b);
f(c);

def replace(a, b, f(c)):
    if (f(a)*f(c) > 0):
        b = c
        return b
    else:
        a = c
        return a


#   ************ Get(ROOT) ************************************************

while (f(x) != 0.86547403310161444662):
    if (f(a)*f(b) < 0):
        itr++
        replace(a, b, f(c));
        f(a);
        f(b);
        see(a,b);
        f(c);
    else:
        itr++
        c = (.5*f(b)*a - f(a)*b)/(.5*f(b) - f(a))
        if (f(a)*f(b) < 0):
            replace(a, b, f(c));
            f(a);
            f(b);
            see(a, b);
            f(c);
        else:
            itr++
            c = (f(b)*a - .5*f(a)*b)/(f(b) - .5*f(a))
            replace(a, b, f(c));
            f(a);
            f(b);
            see(a, b);
            f(c);
            
print "x = " + str(c)




#   **********************************************************************



