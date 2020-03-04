x=input()
x=int(x)
end = float()
end1 = float()
end2 = float()
list1 = []
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
print(
    j for j in list1)
