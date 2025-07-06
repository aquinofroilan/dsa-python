
from collections import deque
from sys import path
import os
path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tree_data_structures.utils.node import Node
from tree_data_structures.utils.populate_tree import populate_tree

def breadth_first_search_iteration(node: Node):
    bfs_queue = deque()
    visited = []
    bfs_queue.append(node)
    while bfs_queue:
        visited_node = bfs_queue.popleft()
        visited.append(visited_node.value)
        if visited_node.get_left_node(): bfs_queue.append(visited_node.get_left_node())
        if visited_node.get_right_node(): bfs_queue.append(visited_node.get_right_node())
    return visited

def breadth_first_search_recursive(node: Node):
    visited_set = []
    visited_set.append(node.value)

def main():
    root_node = populate_tree()
    order = breadth_first_search_iteration(root_node)
    print(order)

if __name__ == "__main__":
    main()
