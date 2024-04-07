import heapq
import time

# 定义移动方向和对应的移动操作
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# directions = ['u', 'd', 'l', 'r']

# 将网格转换成字符串形式
def grid_to_str(grid):
    return ''.join(grid)

# 判断当前网格是否为目标网格
def is_target(grid):
    return grid == '12345678x'

# 获取空格的位置
def get_blank_pos(grid):
    return grid.index('x')

# 获取可以移动的位置
def get_adjacent_positions(grid, pos):
    x, y = pos // 3, pos % 3
    adj_positions = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            adj_positions.append(nx * 3 + ny)
    return adj_positions

# 定义启发函数（曼哈顿距离）
def heuristic(grid):
    distance = 0
    for i in range(9):
        if grid[i] != 'x':
            num = int(grid[i])
            distance += abs(i // 3 - (num - 1) // 3) + abs(i % 3 - (num - 1) % 3)
    return distance

def is_solvable(grid):
    # 计算逆序数对的个数
    inversions = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if grid[i] != 'x' and grid[j] != 'x' and grid[i] > grid[j]:
                inversions += 1

    # 根据逆序数对的奇偶性判断是否可解
    return inversions % 2 == 0

# 执行A*搜索
def astar(grid):
    if is_solvable(grid) == False:
        return "unsolvable"
    else:
        queue = []
        heapq.heappush(queue, (0, grid, ''))
        visited = set()
        while queue:
            _, curr_grid, path = heapq.heappop(queue)

            if is_target(curr_grid):
                return path
            curr_grid_str = grid_to_str(curr_grid)
            if curr_grid_str in visited:
                continue
            visited.add(curr_grid_str)

            blank_pos = get_blank_pos(curr_grid)
            for adj_pos in get_adjacent_positions(curr_grid, blank_pos):
                new_grid = list(curr_grid)
                new_grid[blank_pos], new_grid[adj_pos] = new_grid[adj_pos], new_grid[blank_pos]
                new_grid_str = grid_to_str(new_grid)
                if new_grid_str not in visited:
                    if adj_pos - blank_pos == 1:
                        heapq.heappush(queue, (heuristic(new_grid_str) + len(path), new_grid_str, path + 'r'))
                    elif adj_pos - blank_pos == -1:
                        heapq.heappush(queue, (heuristic(new_grid_str) + len(path), new_grid_str, path + 'l'))
                    elif adj_pos - blank_pos == -3:
                        heapq.heappush(queue, (heuristic(new_grid_str) + len(path), new_grid_str, path + 'u'))
                    elif adj_pos - blank_pos == 3:
                        heapq.heappush(queue, (heuristic(new_grid_str) + len(path), new_grid_str, path + 'd'))                   

# 读取输入并执行A*搜索
initial_grid = input().split()
initial_grid = ''.join(initial_grid)
result = astar(initial_grid)
print(result)
