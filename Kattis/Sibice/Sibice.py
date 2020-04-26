import math
n, w, h = input().split(" ")
n = int(n)
w = int(w)
h = int(h)
temp = []
for i in range(0,n):
    z = input()
    temp.append(z)
maxl = math.sqrt(w**2 + h**2)
intlist = list(map(int, temp))
for i in intlist:
    if i > maxl:
        print("NE")
    else:
        print("DA")