'''
Find shortest path from top left column to the right lowest column using DFS.
only step on the columns whose value is 1
if there is no path, it returns -1
(The first column(top left column) is not included in the answer.)

Ex 1)
If maze is
[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]],
the answer is: 14

Ex 2)
If maze is
[[1,0,0],
 [0,1,1],
 [0,1,1]],
the answer is: -1
'''


def find_path(maze):
    return dfs(maze, 0, 0, 0, -1)


def dfs(maze, i, j, depth, cnt):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    row = len(maze)
    col = len(maze[0])

    if i == row - 1 and j == col - 1:
        if cnt != -1 and cnt > depth or cnt == -1:
            cnt = depth
        return cnt

    maze[i][j] = 0

    for direction in directions:
        nx_i = i + direction[0]
        nx_j = j + direction[1]

        if (
            nx_i >= 0
            and nx_i < row
            and nx_j >= 0
            and nx_j < col
            and maze[nx_i][nx_j] == 1
        ):
            cnt = dfs(maze, nx_i, nx_j, depth + 1, cnt)

    maze[i][j] = 1

    return cnt
