def pgen(factor):
    pmax=str(factor**2)
    half_palindrome=int(pmax[0:len(pmax)/2]) -1
    for x in xrange(half_palindrome, 0, -1):
        yield int(str(x) + str(x)[::-1])

def palin(factor):
    for palindrome in pgen(factor):
        for f1 in xrange(factor/11*11, factor/10, -11):
            f2=palindrome/f1
            if f2 > factor:
                break
            if f2*f1==palindrome:
                return palindrome, f1, f2

def biggest(bil):  
    if bil == 1:
        print 9
    elif bil == 2:
        print palin(99)[0]
    elif bil == 3:
        print palin(999)[0]
    elif bil == 4:
        print palin(9999)[0]      

biggest(int(input("bilangan: ")))