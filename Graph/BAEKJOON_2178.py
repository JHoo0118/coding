# N×M크기의 배열로 표현되는 미로가 있다.
# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야
# 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때,
# 서로 인접한 칸으로만 이동할 수 있다. 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다.
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 예제 입력              예제 출력
# 4 6                    15
# 101111
# 101010
# 101011
# 111011

from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
start = (0, 0)
end = (N - 1, M - 1)


def walkable(maze, row, col):
    if row < 0 or row >= len(maze):
        return False
    if col < 0 or col >= len(maze[0]):
        return False
    return maze[row][col]


def get_walkable_neighbours(maze, row, col):
    return [
        (r, c)
        for r, c in [(row, col - 1), (row - 1, col), (row + 1, col), (row, col + 1)]
        if walkable(maze, r, c)
    ]


def shortest_path(maze, start, end):
    seen = set()
    queue = deque([(start, 1)])
    while queue:
        coords, count = queue.popleft()
        if coords == end:
            return count
        if coords not in seen:
            seen.add(coords)
        neighbours = get_walkable_neighbours(maze, coords[0], coords[1])
        print("neighbours: {0}".format(neighbours))
        queue.extend(
            (neighbour, count + 1) for neighbour in neighbours if neighbour not in seen
        )


print(shortest_path(maze, start, end))
