key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]


def rotation_right(key):
    key[:] = [list(a) for a in zip(*key[::-1])]
    return key


def rotation_left(key):
    key[:] = zip(*key[:])
    key[:] = key[::-1]
    return key


def rotate_right(key):
    key.reverse()
    for i in range(len(key)):
        for j in range(i):
            key[i][j], key[j][i] = key[j][i], key[i][j]
    return key

