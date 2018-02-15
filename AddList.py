import numpy as np

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

addList(np.array([1,2,3]),np.array([4,5,6]))



