import numpy as np
import pandas as pd

def addList(arg1,arg2):

    Len1 = len(arg1)
    Len2 = len(arg2)

    if Len1 == Len2:
        totalList = np.array(arg1) + np.array(arg2)
        print(totalList)
        return(totalList)
    else:
        print('None')
        return()

x = input('xの値')
y = input('yの値')
z = input('z')
a = input('a')
b = input('b')
c = input('c')

x = int(x)
y = int(y)
z = int(z)
a = int(a)
b = int(b)
c = int(c)

addList(np.array([x,y,z]),np.array([a,b,c]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()


