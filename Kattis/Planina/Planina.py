a=input()
a=int(a)
N = ''
if a >= 1 and a <= 15:
    N = 4**a + 2**(a+1) + 1
    print (N)
else:
    raise Exception()