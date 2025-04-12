import heapq
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 5, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

start_vertex = 'A'
end_vertex = 'D'

shortest_distances = dijkstra(graph, start_vertex)
shortest_path_length = shortest_distances[end_vertex]

path = []
current_vertex = end_vertex
while current_vertex != start_vertex:
    path.insert(0, current_vertex)
    for neighbor, weight in graph[current_vertex].items():
        if shortest_distances[current_vertex] == shortest_distances[neighbor] + weight:
            current_vertex = neighbor
            break
path.insert(0, start_vertex)


print("Shortest path from {} to {} is:".format(start_vertex, end_vertex))
print(" -> ".join(path))
print("Shortest path length:", shortest_path_length)
