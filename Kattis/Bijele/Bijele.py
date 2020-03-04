a = input()
lista = a.split()
newlist = []
for i in range(0,len(lista)):
    stclist = [1,1,2,2,2,8]
    newlist.append(int(stclist[i]) - int(lista[i]))
print(" ".join([str(x) for x in newlist]))