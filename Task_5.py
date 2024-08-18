import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [visited_nodes.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def bfs(root):
    queue = deque([root])
    visited = {}
    color_map = list(mcolors.CSS4_COLORS.keys())

    i = 0
    while queue:
        node = queue.popleft()
        node.color = mcolors.CSS4_COLORS[color_map[i]]
        visited[node.id] = node.color
        i += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    draw_tree(root, visited)

def dfs(root):
    stack = [root]
    visited = {}
    color_map = list(mcolors.CSS4_COLORS.keys())

    i = 0
    while stack:
        node = stack.pop()
        node.color = mcolors.CSS4_COLORS[color_map[i]]
        visited[node.id] = node.color
        i += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    draw_tree(root, visited)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходів
print("Обхід в ширину (BFS):")
bfs(root)

print("Обхід в глибину (DFS):")
dfs(root)
