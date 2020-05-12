a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

A = []
A.extend([a,b,c])
n = 0

n = A[1] - A[0]
if A[2] - A[1] > n:
    n = A[2] - A[1]

print(n -1)
