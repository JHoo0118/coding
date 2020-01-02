key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotation_right(key):
    key[:] = [list(a) for a in zip(*key[::-1])]
    return key


def rotation_left(key):
    key[:] = [list(a) for a in zip(*key[:])]
    key[:] = key[::-1]
    return key


def move_right(key):
    for i in range(0, len(key)):
        for j in range(len(key[0]) - 2, -1, -1):
            key[i][j + 1] = key[i][j]
            if j == 0:
                key[i][j] = 0
    return key


def move_left(key):
    for i in range(0, len(key)):
        for j in range(0, len(key)):
            if j == len(key) - 1:
                key[i][j] = 0
            else:
                key[i][j] = key[i][j + 1]
    return key


def move_up(key):
    key = rotation_right(key)
    key = move_right(key)
    key = rotation_left(key)

    return key


def move_down(key):
    key = rotation_right(key)
    key = move_left(key)
    key = rotation_left(key)

    return key


def check(key):
    pass


print(key[1][0] and lock[1][0])
