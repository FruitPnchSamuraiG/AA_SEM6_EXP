
graph = [[0, 8, 10, 0, 0, 0], 
            [0, 0, 0, 2, 7, 0],
            [0, 3, 0, 0, 12, 0],
            [0, 0, 0, 0, 0, 10],
            [0, 0, 0, 4, 0, 8], 
            [0, 0, 0, 0, 0, 0]]
source = 0
sink = len(graph) - 1

def initialize_graph(graph):
    residual_graph = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            residual_graph[i][j] = graph[i][j]
            
    return residual_graph


def find_augmenting_path(residual_graph):
    visited = [False] * len(residual_graph)
    return dfs(residual_graph, visited, source, [])


def dfs(residual_graph, visited, current, path):
    visited[current] = True
    path.append(current)
    if current == sink:
        return path
    for neighbor in range(len(residual_graph[current])):
        if not visited[neighbor] and residual_graph[current][neighbor] > 0:
            result = dfs(residual_graph, visited, neighbor, path)
            if result:
                return result
    path.pop()
    return None


def calculate_bottleneck_capacity(residual_graph, path):
    bottleneck = float('inf')
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        bottleneck = min(bottleneck, residual_graph[u][v])
    return bottleneck

def update_residual_graph(residual_graph, path, bottleneck):
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        residual_graph[u][v] -= bottleneck
        residual_graph[v][u] += bottleneck
        
        
def ford_fulkerson(graph):
    residual_graph = initialize_graph(graph)
    print(residual_graph)
    max_flow = 0
    while True:
        path = find_augmenting_path(residual_graph)
        if not path:
            break
        bottleneck = calculate_bottleneck_capacity(residual_graph, path)
        max_flow += bottleneck
        update_residual_graph(residual_graph, path, bottleneck)
        
    return max_flow

max_flow = ford_fulkerson(graph)
print("Max Flow:", max_flow)

###############################################################################################################3
# graph = [[0, 8, 10, 0, 0, 0], 
#             [0, 0, 0, 2, 7, 0],
#             [0, 3, 0, 0, 12, 0],
#             [0, 0, 0, 0, 0, 10],
#             [0, 0, 0, 4, 0, 8], 
#             [0, 0, 0, 0, 0, 0]]

# source  = 0
# sink = len(graph)-1

# def intialize_graph(graph):
#     residual_graph = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    
#     for i in range(len(graph)):
#         for j in range(len(graph[i])):
#             residual_graph[i][j] = graph[i][j]
            
#     return residual_graph


# def aug_path(residual_graph):
#     visited = [False] * len(residual_graph)
#     return dfs(residual_graph, visited, source, [])


# def dfs(residual_graph, visited, current, path):
#     visited[current] = True
#     path.append(current)
    
#     if current == sink:
#         return path
    
#     for neighbour in range(len(residual_graph)):
#         if not visited[neighbour] and residual_graph[current][neighbour] > 0:
#             result = dfs(residual_graph, visited, neighbour, path)
#             if result:
#                 return result
        
#     path.pop()
#     return None

# def bottleneck(residual_graph, path):
#     min_capacity = float('inf')
#     for i in range(len(path)-1):
#         u, v = path[i], path[i+1]
#         min_capacity = min(min_capacity, residual_graph[u][v])

#     return min_capacity
    
    
# def update_graph(residual_graph, bottle_neck, path):
#     for i in range(len(path)-1):
#         u, v = path[i], path[i+1]
#         residual_graph[u][v] += bottle_neck
#         residual_graph[v][u] -= bottle_neck



# def ff(graph):
#     max_flow = 0
#     residual = intialize_graph(graph)
#     print(residual)
#     while True: 
#         path = aug_path(residual)
#         if not path:
#             break
#         bottle = bottleneck(residual, path)
#         max_flow  += bottle
#         print(max_flow)
#         update_graph(residual, bottle, path)
#     return max_flow

        
# max_flow = ff(graph)
# print("Max Flow:", max_flow)
