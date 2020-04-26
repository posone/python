n, h, v = input().split(" ")
n = int(n)
h = int(h)
v = int(v)
a = n - v
b = n - h
tablica = [v*h*4, v*b*4, a*h*4, a*b*4]
print(max(tablica))