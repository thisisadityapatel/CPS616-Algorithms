import collections

graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 5],
    4: [2, 6],
    5: [3, 7, 8],
    6: [4, 7],
    7: [5, 6],
    8: [5],
}

#      1
#     / \
#    2 - 3
#   /     \
#  4       5
#   \     / \
#    6 - 7   8

graph2 = {
    1: [2, 3],
    2: [1, 3, 4, 5],
    3: [1, 2, 5, 7, 8],
    4: [2],
    5: [2, 3, 6],
    6: [5],
    7: [3, 8],
    8: [3, 7]
}

#    7───8
#     \ /
#      3───5───6
#     / \
#    1───2───4

def bfs(graph, start):
    queue = collections.deque()
    if start:
        queue.append(start)
    output = []
    status = {}
    dist = collections.defaultdict(int)
    dist[start] = 0
    for node in graph.keys():
        status[node] = "white"
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if status[node] != "black":
                status[node] = "red"
                output.append(node)
                for child_node in graph[node]:
                    if status[child_node] == "white":
                        dist[child_node] += dist[node] + 1
                        status[child_node] = "red"
                        queue.append(child_node)
                status[node] = "black"
    print(output)
    print(dist)
    return output

if __name__ == "__main__":
    bfs(graph, 1)
    bfs(graph2, 1)