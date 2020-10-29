d = []
C, X, M = input().split(' ')
C = float(C)
X = float(X)
M = float(M)

for i in range(0, 6):
    a, b = input().split(' ')
    d.extend([a, b])

d = list(map(float,d))
#print(d, C, X, M)
SpeedList = []

for i in range(0,len(d),2):
    Time = round(M / d[i], 6)
    OnGas = round(M / d[i + 1], 6)
    G = round(C/2 - X * Time, 6)
    #print (Time, OnGas, G)
    if G > OnGas:
        SpeedList.append(int(d[i]))
#print(SpeedList)
if len(SpeedList) > 0:
    print ("YES", max(SpeedList))
else:
    print ("NO")
