a, b, c = input().split(' ')
i, j, k = input().split(' ')
JUICE = []
JUICE.extend(map(int, [a, b, c]))
RATIO = []
RATIO.extend(map(int, [i, j, k]))
Rmin = min(JUICE[i]/RATIO[i] for i in range(0,3))
T = [round(JUICE[i] - Rmin*RATIO[i], 4) for i in range(0,3)]
print(*T, sep=" ")
