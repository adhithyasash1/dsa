def yo(L):
    a = type(L[0])
    count = len(L)
    if a == type(L[1]):
        for i in range(count):
            if a == type(L[i]):
                pass
            else:
                return L[i]
    else:
        return L[0]

def odd_one(L):
    x = yo(L)
    if type(x) == type('yo'):
        return('str')
    if type(x) == type(1):
        print('int')
    if type(x) == type(0.5):
        print('float')
    if type(x) == type(True):
        print('bool')
    