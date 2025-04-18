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


def dfs(graph, start):
    status = {}
    for node in graph.keys():
        status[node] = "white"
    output = []

    def traversal(node):
        if status[node] != "black":
            output.append(node)
            status[node] = "red"
            for child in graph[node]:
                if status[child] == "white":
                    status[child] = "red"
                    traversal(child)
            status[node] = "black"

    traversal(start)
    return output


print(dfs(graph, 1))
