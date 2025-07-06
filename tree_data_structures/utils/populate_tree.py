"""
           99
         /    \
       55      25
     /   \    /   \
   33   44  12   37
  / \   / \ / \   / \
22 31 41 47 8 15 28 42

"""

from tree_data_structures.utils.node import Node

def populate_tree():
    node = Node(99)
    level_2_left_node = node.set_left_node(Node(55))
    level_2_right_node = node.set_right_node(Node(25))

    level_3_left_left = level_2_left_node.set_left_node(Node(33))
    level_3_left_right = level_2_left_node.set_right_node(Node(44))

    level_3_right_left = level_2_right_node.set_left_node(Node(12))
    level_3_right_right = level_2_right_node.set_right_node(Node(37))

    level_4_ll_left = level_3_left_left.set_left_node(Node(22))
    level_4_ll_right = level_3_left_left.set_right_node(Node(31))

    level_4_lr_left = level_3_left_right.set_left_node(Node(41))
    level_4_lr_right = level_3_left_right.set_right_node(Node(47))

    level_4_rl_left = level_3_right_left.set_left_node(Node(8))
    level_4_rl_right = level_3_right_left.set_right_node(Node(15))

    level_4_rr_left = level_3_right_right.set_left_node(Node(28))
    level_4_rr_right = level_3_right_right.set_right_node(Node(42))
    print("Tree Structure:")
    print(f"Root: {node.value}")
    print(f"Level 2: {level_2_left_node.value}, {level_2_right_node.value}")
    print(f"Level 3: {level_3_left_left.value}, {level_3_left_right.value}, {level_3_right_left.value}, {level_3_right_right.value}")
    print(f"Level 4: {level_4_ll_left.value}, {level_4_ll_right.value}, {level_4_lr_left.value}, {level_4_lr_right.value}, "
          f"{level_4_rl_left.value}, {level_4_rl_right.value}, {level_4_rr_left.value}, {level_4_rr_right.value}")
    return node
