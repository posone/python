x = input()
x = int(x)
temp = []
for i in range(0,x):
    z = input()
    temp.append(z)
razem = []
for z in temp:
    power = z[len(z)-1]
    power = int(power)
    num = z[:len(z)-1]
    num = int(num)
    suma = num ** power
    razem.append(suma)
print(sum(razem))

