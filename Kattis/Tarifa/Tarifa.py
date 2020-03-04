Pm = input()
Pm = int(Pm)
Nm = input()
Nm = int(Nm)
templist = []
for i in range(0,Nm):
    a = input()
    a = int(a)
    b = Pm - a
    templist.append(b)
print(sum(templist)+Pm)
