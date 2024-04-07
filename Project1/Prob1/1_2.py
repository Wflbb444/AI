#稠密图，邻接矩阵
def naive_dijkstra(n, edges):
    graph = [[] for _ in range(n + 1)]
    for x, y, z in edges:
        graph[x].append((y, z))

    # 初始化距离数组，初始距离为无穷大
    distance = [float('inf')] * (n + 1)
    distance[1] = 0

    # 记录已经访问过的节点
    visited = [False] * (n + 1)

    for _ in range(n):
        # 选择未访问的距离最小的节点
        min_dist = float('inf')
        min_node = -1
        for i in range(1, n + 1):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_node = i

        if min_node == -1:
            break

        visited[min_node] = True

        # 更新与当前节点相邻节点的距离
        for neighbor, weight in graph[min_node]:
            if distance[min_node] + weight < distance[neighbor]:
                distance[neighbor] = distance[min_node] + weight

    return distance[n] if distance[n] != float('inf') else -1
# 读取输入
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 输出最短距离
print(naive_dijkstra(n, edges))