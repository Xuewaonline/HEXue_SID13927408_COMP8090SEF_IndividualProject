"""
Graph Data Structure
COMP8090SEF - Task 2 Self Study
Student: HE Xue (SID: 13927408)

This module implements three types of graphs:
1. Undirected Graph - edges have no direction
2. Directed Graph - edges have direction
3. Weighted Graph - edges have weights
"""

from collections import deque


class UndirectedGraph:
    """
    Undirected Graph using adjacency list.
    Edges are bidirectional (A-B means B-A too).
    Example: Social network friendships
    """

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()

    def add_edge(self, v1, v2):
        """Add an undirected edge between v1 and v2."""
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1].add(v2)
        self.adj_list[v2].add(v1)

    def has_edge(self, v1, v2):
        """Check if an edge exists between v1 and v2."""
        return v1 in self.adj_list and v2 in self.adj_list[v1]

    def get_neighbors(self, vertex):
        """Return neighbors of a vertex."""
        return self.adj_list.get(vertex, set())

    def bfs(self, start):
        """
        Breadth-First Search (BFS).
        Explores level by level using a queue.
        """
        if start not in self.adj_list:
            return []
        
        visited = set()
        order = []
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in sorted(self.adj_list[vertex]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        """
        Depth-First Search (DFS).
        Explores as deep as possible first using a stack.
        """
        if start not in self.adj_list:
            return []
        
        visited = set()
        order = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                for neighbor in sorted(self.adj_list[vertex], reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def display(self):
        """Print the adjacency list."""
        print("  Undirected Graph:")
        for vertex in sorted(self.adj_list):
            print(f"    {vertex} -> {sorted(self.adj_list[vertex])}")


class DirectedGraph:
    """
    Directed Graph using adjacency list.
    Edges have direction (A->B does NOT mean B->A).
    Example: Task dependencies, web links
    """

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()

    def add_edge(self, source, destination):
        """Add a directed edge from source to destination."""
        self.add_vertex(source)
        self.add_vertex(destination)
        self.adj_list[source].add(destination)

    def has_edge(self, source, destination):
        """Check if directed edge exists."""
        return source in self.adj_list and destination in self.adj_list[source]

    def in_degree(self, vertex):
        """Count edges coming into vertex."""
        return sum(1 for v in self.adj_list if vertex in self.adj_list[v])

    def out_degree(self, vertex):
        """Count edges going out from vertex."""
        return len(self.adj_list.get(vertex, set()))

    def topological_sort(self):
        """
        Return topological ordering (execution order).
        Uses Kahn's algorithm. Returns None if cycle exists.
        """
        # Calculate in-degrees
        in_deg = {v: 0 for v in self.adj_list}
        for v in self.adj_list:
            for neighbor in self.adj_list[v]:
                in_deg[neighbor] += 1

        # Start with vertices having no prerequisites
        queue = deque([v for v in in_deg if in_deg[v] == 0])
        order = []

        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self.adj_list[vertex]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    queue.append(neighbor)

        # Check if all vertices were processed
        if len(order) != len(self.adj_list):
            return None  # Cycle detected
        return order

    def display(self):
        """Print the adjacency list."""
        print("  Directed Graph:")
        for vertex in sorted(self.adj_list):
            print(f"    {vertex} -> {sorted(self.adj_list[vertex])}")


class WeightedGraph:
    """
    Weighted Graph using adjacency list with weights.
    Can be undirected or directed.
    Example: GPS navigation (shortest path)
    """

    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}

    def add_edge(self, v1, v2, weight):
        """Add a weighted edge."""
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1][v2] = weight
        if not self.directed:
            self.adj_list[v2][v1] = weight

    def get_weight(self, v1, v2):
        """Get weight of edge between v1 and v2."""
        if v1 in self.adj_list and v2 in self.adj_list[v1]:
            return self.adj_list[v1][v2]
        return None

    def dijkstra(self, start):
        """
        Dijkstra's algorithm for shortest paths.
        Returns dictionary of {vertex: shortest_distance}.
        """
        if start not in self.adj_list:
            return {}

        # Initialize distances
        distances = {v: float('inf') for v in self.adj_list}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.adj_list):
            # Find unvisited vertex with smallest distance
            current = None
            for v in self.adj_list:
                if v not in visited:
                    if current is None or distances[v] < distances[current]:
                        current = v

            if current is None or distances[current] == float('inf'):
                break

            visited.add(current)

            # Update distances to neighbors
            for neighbor, weight in self.adj_list[current].items():
                new_dist = distances[current] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist

        return distances

    def display(self):
        """Print the adjacency list with weights."""
        graph_type = "Directed" if self.directed else "Undirected"
        print(f"  Weighted {graph_type} Graph:")
        for vertex in sorted(self.adj_list):
            edges = ", ".join(f"{n}(w={w})" for n, w in sorted(self.adj_list[vertex].items()))
            print(f"    {vertex} -> [{edges}]")


# ============== DEMONSTRATIONS ==============

def demo_undirected():
    """Demo: Undirected Graph - Friendship Network"""
    print("\n" + "=" * 50)
    print("  DEMO 1: Undirected Graph - Friendship Network")
    print("=" * 50)

    g = UndirectedGraph()
    g.add_edge("Alice", "Bob")
    g.add_edge("Alice", "Charlie")
    g.add_edge("Bob", "Diana")
    g.add_edge("Charlie", "Diana")
    g.add_edge("Diana", "Eve")

    g.display()
    print(f"\n  Alice's friends: {sorted(g.get_neighbors('Alice'))}")
    print(f"  Alice and Bob are friends: {g.has_edge('Alice', 'Bob')}")
    print(f"  BFS from Alice: {g.bfs('Alice')}")
    print(f"  DFS from Alice: {g.dfs('Alice')}")


def demo_directed():
    """Demo: Directed Graph - Task Dependencies"""
    print("\n" + "=" * 50)
    print("  DEMO 2: Directed Graph - Task Dependencies")
    print("=" * 50)

    g = DirectedGraph()
    g.add_edge("Requirements", "Design")
    g.add_edge("Design", "Implement")
    g.add_edge("Design", "Test Plan")
    g.add_edge("Implement", "Test")
    g.add_edge("Test Plan", "Test")
    g.add_edge("Test", "Deploy")

    g.display()
    print(f"\n  In-degree of Test: {g.in_degree('Test')} (prerequisites)")
    print(f"  Out-degree of Design: {g.out_degree('Design')} (enables)")
    print(f"  Topological order: {g.topological_sort()}")


def demo_weighted():
    """Demo: Weighted Graph - City Distances"""
    print("\n" + "=" * 50)
    print("  DEMO 3: Weighted Graph - City Distances")
    print("=" * 50)

    g = WeightedGraph(directed=False)
    g.add_edge("HK", "Shenzhen", 30)
    g.add_edge("HK", "Macau", 65)
    g.add_edge("Shenzhen", "Guangzhou", 140)
    g.add_edge("Macau", "Guangzhou", 145)
    g.add_edge("Guangzhou", "Changsha", 660)

    g.display()
    print(f"\n  Shortest distances from HK:")
    distances = g.dijkstra("HK")
    for city, dist in sorted(distances.items()):
        print(f"    To {city}: {dist} km")


if __name__ == "__main__":
    print("\n" + "#" * 50)
    print("  GRAPH DATA STRUCTURE DEMONSTRATIONS")
    print("#" * 50)

    demo_undirected()
    demo_directed()
    demo_weighted()

    print("\n" + "=" * 50)
    print("  All demonstrations completed!")
    print("=" * 50)
