import heapq

def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Відстань до початкової вершини 0

    # Ініціалізуємо чергу пріоритетів (бінарну купу)
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)  # Перетворюємо список на бінарну купу

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань до поточної вершини більше відомої, продовжуємо
        if current_distance > distances[current_vertex]:
            continue

        # Переглядаємо сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдена коротша відстань, оновлюємо її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

# Виведення найкоротших шляхів від початкової вершини
for vertex, distance in shortest_paths.items():
    print(f"Найкоротший шлях від {start_vertex} до {vertex}: {distance}")
