import math
a,b=input().split(' ')
a = float(a)
b = float(b)
y = math.ceil(a * (b - 0.99))
print(y)