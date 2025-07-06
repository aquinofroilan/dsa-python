class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def set_left_node(self, value):
        self.left_node = value
        return self.left_node

    def set_right_node(self, value):
        self.right_node = value
        return self.right_node

    def get_right_node(self):
        return self.right_node

    def get_left_node(self):
        return self.left_node

    def __str__(self):
        return f"Node(value={self.value})"

    def __repr__(self):
        return self.__str__()

