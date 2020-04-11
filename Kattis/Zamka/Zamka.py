L = input()
D = input()
X = input()
L = int(L)
D = int(D)
X = int(X)
NUM = {i : sum(map(int, str(i))) for i in range(L, D + 1) if sum(map(int, str(i))) == X}
print(min(NUM.keys()))
print(max(NUM.keys()))
