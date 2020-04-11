a,b=input().split(' ')
a=str(a)[::-1]
b=str(b)[::-1]
if int(a) > int(b):
    print(a)
else:
    print(b)