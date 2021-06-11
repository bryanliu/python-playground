class UnionFind:
    def __init__(self):
        self.parents = {}

    def find(self, x):
        pass

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parents[x] = y

    def connect(self, x, y):
        return self.find(x) == self.find(y)


def main(matrix):
    if not matrix or not matrix[0]: return []
    m, n = len(matrix), len(matrix[0])
    # hill  1, dale -1

    uf = UnionFind()

    def getid(i, j, idx):
        return (m * i + j) * 4 + idx

    # step 1: connect neighbours
    for i in range(m):
        for j in range(n):

            if matrix[i][j] == 1:
                uf.union(getid(i, j, 0), getid(i, j, 1))
                uf.union(getid(i, j, 2), getid(i, j, 3))

            if i > 0:
                uf.union(getid(i, j, 0), getid(i - 1, j, 2))

            if j > 0:
                uf.union(getid(i, j, 1), getid(i, j - 1, 3))

    # step 2: check top and bottom connection
    res = [-1] * n
    for i in range(n):

        for j in range(n):
            if uf.connect(getid(0, i, 1), getid(m - 1, j, 3)):
                res[i] = j

    return res
