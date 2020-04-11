x=input()
x=int(x)
end = float()
end1 = float()
end2 = float()
list1 = []
def n_split(iterable, n, fillvalue=None):
    num_extra = len(iterable) % n
    zipped = zip(*[iter(iterable)] * n)
    return zipped if not num_extra else zipped + [iterable[-num_extra:], ]

for i in range(0,x):
    a,b = input().split()
    a = float(a)
    b = float(b)
    end = round(60 * a / b, 4)
    end1 = round(60 * (a - 1) / b, 4)
    end2 = round(60 * (a + 1) / b, 4)
    list1.append(end1)
    list1.append(end)
    list1.append(end2)
for i in n_split(list1, 3):
    print(' '.join(map(str, i)))