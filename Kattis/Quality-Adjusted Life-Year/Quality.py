x=input()
x=int(x)
end = float()
for i in range(0,x):
    a,b = input().split()
    a = float(a)
    b = float(b)
    end += a*b
print(round(end, 3))