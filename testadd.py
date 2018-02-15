import doctest

def Add(x,y):
    x = input('xの値')
    y = input('yの値')
    z = int(x) + int(y)
    print(z)
    return(z)

Add(1,1)

if __name__ == '__main__':
    doctest.testmod(verbose = True)
