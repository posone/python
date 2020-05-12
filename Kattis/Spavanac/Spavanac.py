x, y = input().split(" ")
x = int(x)
y = int(y)
yy = y - 45
xx = 0
if yy < 0:
    yy = 60 - abs(yy)
    if x == 0:
        xx = 23
    else:
        xx = x - 1
else:
    yy = yy
    xx = x

print(xx, yy)