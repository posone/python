s,t,n=input().split(' ')
d = input().split(' ')
dist = list(map(int, d))
b = input().split(' ')
bus = list(map(int, b))
c = input().split(' ')
cint = list(map(int, c))
output = "yes"
firstsum = sum(dist) + sum(bus)
for i in range(0, int(n)):
    temp = cint[i] - dist[i]
    temp2 = + temp
sumofsum = firstsum + temp2
if sumofsum > int(t):
    print("no")
else:
    print("yes")