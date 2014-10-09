__author__ = 'Pavel Rubinson'


def lattice_paths(size):
    mat = [[0 for x in range(size)] for x in range(size)]
    for i in range(size):
        for j in range(size):
            if i == 0 and j == 0:
                mat[i][j] = 1
            elif i != 0 and j != 0:
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
            elif i == 0 and j != 0:
                mat[i][j] = mat[i][j-1]
            elif i != 0 and j == 0:
                mat[i][j] = mat[i-1][j]
    return mat[size-1][size-1]

print(lattice_paths(21))

