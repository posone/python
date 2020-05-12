while True:
    n = input()
    n = int(n)
    listv = []
    lists = [0]
    miles = 0
    miles = int(miles)
    if n == -1:
        break
    else:
        for i in range(0,n):
            v, s = input().split(" ")
            v = int(v)
            s = int(s)
            listv.append(v)
            lists.append(s)
            miles += listv[i] * (lists[i + 1] - lists[i])
    print(miles, "miles")