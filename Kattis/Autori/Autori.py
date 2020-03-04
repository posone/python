w = input()
z=w.replace('-', ' ').split()
inicjal = []
for i in range(len(z)):
    inicjal.append(z[i][0])
print("".join([str(x) for x in inicjal]))