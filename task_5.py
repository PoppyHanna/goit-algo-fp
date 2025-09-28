import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import copy

class Node:
    def __init__(self, key, color="#87CEEB"):
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
        add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
        graph.add_edge(node.id, node.right.id)
        r = x + 1 / 2 ** layer
        pos[node.right.id] = (r, y - 1)
        add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Binary Tree Traversal"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel("X-axis (position of nodes)", fontsize=10)
    plt.ylabel("Y-axis (tree depth)", fontsize=10)

    plt.show()

def bfs_traversal(root):
    if not root:
        return[]
    
    order = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right) 

    return order

def dfs_traversal(root):
    if not root:
        return[]

    order = []
    stack = [root]

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order

def assign_colors(order):
    n = len(order)
    for i, node in enumerate(order):
        intensity = int(50 +(205 * i / (n - 1))) if n > 1 else 255 
        hex_color = f"#{intensity:02X}{intensity:02X}FF"
        node.color = hex_color

root = Node(10)
root.left = Node(7)
root.left.left = Node(5)
root.left.right = Node(6)
root.right = Node(9)
root.right.left = Node(2)  
root.right.right = Node(3)

order_bfs = bfs_traversal(root)
assign_colors(order_bfs)
print("BFS:", [n.val for n in order_bfs])
draw_tree(root, title="BFS Traversal")

order_dfs = dfs_traversal(root)
assign_colors(order_dfs)
print("DFS:", [n.val for n in order_dfs])
draw_tree(root, title="DFS Traversal")
