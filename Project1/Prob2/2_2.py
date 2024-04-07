from collections import deque
# import time
# 定义目标状态
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 'x']
# 定义上、下、左、右四个方向的偏移量
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_solvable(grid):
    # 计算逆序数对的个数
    inversions = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if grid[i] != 'x' and grid[j] != 'x' and grid[i] > grid[j]:
                inversions += 1

    # 根据逆序数对的奇偶性判断是否可解
    return inversions % 2 == 0


def get_adjacent(state):
    #获取当前状态下空格相邻的状态
    adj_states = []
    idx = state.index('x')
    row, col = idx // 3, idx % 3
    # 上下左右移动
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            adj_states.append(new_state)
    return adj_states

def bfs(start_state):
    #BFS求解最小交换次数
    if is_solvable(start_state)==False:
        return -1
    else:
        visited = set([tuple(start_state)])
        queue = deque([(start_state, 0)])  # 使用队列保存状态及其对应的步数
        while queue:
            state, steps = queue.popleft()
            for adj_state in get_adjacent(state):                    
                if adj_state == goal_state:
                    return steps+1
                if tuple(adj_state) not in visited:
                    visited.add(tuple(adj_state))
                    queue.append((adj_state, steps + 1))
                

# 读取输入
start_state = list(input().split())
# start_time=time.perf_counter()
# 转换输入为合适的类型
for i in range(len(start_state)):
    if start_state[i] != 'x':
        start_state[i] = int(start_state[i])
if(start_state == goal_state):
    print(0)
    exit(0)
# 求解并输出结果
print(bfs(start_state))
# end_time=time.perf_counter()
# print(end_time-start_time)