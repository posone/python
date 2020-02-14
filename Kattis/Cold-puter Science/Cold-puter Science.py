n=int(input())
t=list(map(int,input().split(' ')))
print(t)
c=[]
for i in t:
    if i < 0:
        c.append(i)
print(len(c))


n = int(input())
T = list(map(int, input().split(' ')))
print(len([t for t in T if t < 0]))