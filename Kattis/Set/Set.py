import itertools

c = []
for i in range(0, 4):
    a,b,d = input().split(' ')
    c.extend([a, b, d])

empty = []
tosort = []

for i in range(0,12):
    for j in range(i+1, 12):
        for k in range(j+1, 12):
            no1 = no2 = no3 = ''
            for x in range(0,4):
                if (c[i][x] == c[j][x] and c[i][x] == c[k][x] and c[j][x] == c[k][x]) or (c[i][x] != c[j][x] and c[i][x] != c[k][x] and c[j][x] != c[k][x]):
                    no1 += c[i][x]
                    no2 += c[j][x]
                    no3 += c[k][x]
            #print(no1, no2, no3)
            if (len(no1) == len(no2) == len(no3) == 4):
                print(i + 1,  j + 1, k + 1)
                tosort.append([i + 1,  j + 1, k + 1])
                empty.append(1)


if len(empty) == 0: print("no sets")
tosort.sort()
nodup = list(k for k,_ in itertools.groupby(tosort))
for i in nodup:
    toprint = ''
    for j in i:
        toprint = toprint + str(j) + ' '
    #print(toprint)
#   for j in range(0,4):
#        print("ktore karty", cards[i], cards.index(cards[i]), cards[i+1], "ktore cechy", i, j)
#        if cards[i][0] == cards[i+1][0] and cards[i][1] == cards[i+1][1] and cards[i][2] == cards[i+1][2]:
#            print("jesli rowne", cards[i])