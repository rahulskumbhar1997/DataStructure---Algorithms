class Node:

    def __init__(self, node):
        self.mp_next_node = None
        self.mNode = node

    def add_next_node(self, node):
        self.mp_next_node = node

    def get_next_node(self):
        return self.mp_next_node
