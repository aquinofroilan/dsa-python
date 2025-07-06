
from tree_data_structures.utils.node import Node
from tree_data_structures.utils.populate_tree import populate_tree

def depth_first_search(node: Node):
    visited = []


def main():
    root_node = populate_tree()
    order = depth_first_search(root_node)
    print(order)

if __name__ == "__main__":
    main()
