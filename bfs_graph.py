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

def bfs(graph, start) -> list:
    queue = collections.deque()
    queue.append(start)
    output = []

    status = {}
    for node in graph.keys():
        status[node] = "white"

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if status[node] != "black":
                status[node] = "red"
                output.append(node)
                for child in graph[node]:
                    if status[child] == "white":
                        status[child] = "red"
                        queue.append(child)
                status[node] = "black"
    return output


print(bfs(graph, 1))