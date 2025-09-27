import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((v, w))

    def dijkstra(self, start):
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "E", 3)
    g.add_edge("E", "D", 4)
    g.add_edge("D", "F", 11)

    start_node = "A"
    shortest_paths = g.dijkstra(start_node)

    print(f"Shortest paths from vertex {start_node}: ")
    for node, dist in shortest_paths.items():
        print(f"{start_node} -> {node}: {dist}")

