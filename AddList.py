import numpy as np

def addList(arg1,arg2):
    total = arg1 + arg2
    return(total)


totalList = addList(10,20)

print(totalList)

x =  np.array([1,2,3,4])
y = np.array([2,3,4])

LenX = len(x)
LenY = len(y)

if LenX == LenY:
    print(x + y)
else:
    print('None')
