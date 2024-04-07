import heapq
# import time
#优先队列用堆
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
    # 上下左右移动s  
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = list(state)
            new_state[row * 3 + col], new_state[nr * 3 + nc] = new_state[nr * 3 + nc], new_state[row * 3 + col]
            adj_states.append((''.join(new_state), 1)) 
    return adj_states

def dijkstra(start_state):
    if is_solvable(start_state)==False:
        return -1
    else:
        pq = [(0, start_state)]  # 使用优先队列保存状态及其到达该状态的路径长度
        visited = set()
        dist = {start_state: 0}        
        while pq:
            d, state = heapq.heappop(pq)
            if state == '12345678x':
                return dist[state]            
            if state in visited:
                continue           
            visited.add(state)
            for neighbor, weight in get_adjacent(state):
                if neighbor not in dist or d + weight < dist[neighbor]:
                    dist[neighbor] = d + weight
                    heapq.heappush(pq, (dist[neighbor], neighbor))
    
start_state = input().split()
start_state = ''.join(start_state)
# start_time=time.perf_counter()
print(dijkstra(start_state))
# end_time=time.perf_counter()
# print(end_time-start_time)