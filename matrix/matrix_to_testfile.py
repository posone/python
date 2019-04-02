#M = [[1,2,3],[4,5,6],[7,8,9]]
M = "1 2 3\n4 5 6\n7 8 9\n8 7 6"
print(M)

rows = [[i for i in r.split()] for r in M.split("\n")]
col = list(zip(*rows))
#self.columns = list(map(list, zip(*self.rows)))
#rows = [[int(i) for i in r.split()] for r in M.split("\n")]
print (rows)
print (col)
#col3 = [r[1] for r in M]
#col2 = [r[2] for r in M]
#suma1 = sum(col2)


def func(num):
    g=(lambda x:1   )
    return g(num)
print(func(5))


class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [map(int, r.split()) for r in matrix_string.split('\n')]

    def row(self):
        return self._matrix[:]

    def column(self):
        return map(list, zip(*self._matrix))
