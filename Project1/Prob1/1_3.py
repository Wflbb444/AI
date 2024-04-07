import heapq
#稀疏图
def heap_dijkstra(n, edges):
    graph = [[] for _ in range(n + 1)]
    for x, y, z in edges:
        graph[x].append((y, z))

    # 初始化距离数组，初始距离为无穷大
    distance = [float('inf')] * (n + 1)
    distance[1] = 0

    # 使用优先队列来维护当前最小距离的节点，时间复杂度O()nlogn
    pq = [(0, 1)]  # (距离, 节点)
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distance[node]:
            continue
        for neighbor, weight in graph[node]:
            if distance[node] + weight < distance[neighbor]:
                distance[neighbor] = distance[node] + weight
                heapq.heappush(pq, (distance[neighbor], neighbor))

    return distance[n] if distance[n] != float('inf') else -1
# 读取输入
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 输出最短距离
print(heap_dijkstra(n, edges))