# 可解性判断

# 把除x外的所有数字排成一个序列，求序列的逆序对数。逆序对数指对于第i 个数，后面有多少个数比它小。例如，对于1 2 3 x 4 6 75 8，6后面有一个数5比它小，6和5是一个逆序对，7后面有一个数5比它小，7和5是一个逆序对，该序列共两个逆序对。数码问题可以被看作N ×N 的棋盘，八数码问题N =3，十五数码问题N =4。对于每一次交换操作，左右交换都不改变逆序对数，上下交换时逆序对数增加(N-1)、减少(N -1)或不变。

# N 为奇数时：上下交换时每次增加或减少的逆序对数都为偶数，因此每次移动逆序对数，奇偶性不变。若初态的逆序对数与目标状态的逆序对数的奇偶性相同，则有解。
# N 为偶数时：上下交换时每次增加或减少的逆序对数都为奇数，上下交换一次，奇偶性改变一次。因此需要计算初态和目标状态x相差的行数k ，若初态的逆序对数加上k 与目标状态逆序对数奇偶性相同，则有解。
# 八数码问题N =3，若初态的逆序对数与目标状态逆序对数奇偶性相同，则有解。本题目标状态的逆序对数为0，因此初态的逆序对数必须为偶数才有解。注意：统计逆序对数时x除外。

# def is_solvable(grid):
#     # 计算逆序数对的个数
#     inversions = 0
#     for i in range(9):
#         for j in range(i + 1, 9):
#             if grid[i] != 'x' and grid[j] != 'x' and grid[i] > grid[j]:
#                 inversions += 1

#     # 根据逆序数对的奇偶性判断是否可解
#     return inversions % 2 == 0

from collections import deque


def dfs(grid):
    goal_state = '12345678x'
    visited = set()
    queue = deque([(grid, grid.index('x'))])

    while queue:
        curr_grid, pos_x = queue.pop()
        if curr_grid == goal_state:
            return True

        if curr_grid in visited:
            continue

        visited.add(curr_grid)

        x, y = pos_x // 3, pos_x % 3
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_pos_x = nx * 3 + ny
                new_grid = list(curr_grid)
                new_grid[pos_x], new_grid[new_pos_x] = new_grid[new_pos_x], new_grid[pos_x]
                new_grid_str = ''.join(new_grid)
                if new_grid_str not in visited:
                    queue.append((new_grid_str, new_pos_x))

    return False

# 读取初始网格
grid = input().split()
grid = ''.join(grid)
# 检查是否可解
if dfs(grid):
    print(1)
else:
    print(0)
