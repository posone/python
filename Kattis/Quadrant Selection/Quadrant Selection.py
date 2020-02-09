x=input()
x = int(x)
y=input()
y= int(y)
Q = ''
if x > 0 and y > 0:
    Q = 1
    print (Q)
if x > 0 and y < 0:
    Q = 4
    print(Q)
if x < 0 and y < 0:
    Q = 3
    print(Q)
if x < 0 and y > 0:
    Q = 2
    print(Q)
if x == 0 or y == 0:
    raise Exception('Wrong Value')