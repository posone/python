a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

A = []
A.extend([a,b,c])
n = 0

while True:
    if A[1] > A[0] and A[2] > A[1]:
        n += 1
        A[0] = A[1] + 1
        A.sort()
        print(A)
        if A[0] + 1 == A[1] and A[1] + 1 == A[2]:
            print(n)
            break
    else:
        print(n)
        break
