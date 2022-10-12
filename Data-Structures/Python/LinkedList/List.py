from Node import Node


class List:

    def __init__(self, node: Node):
        self.m_head_node = node

    def get_tail_node(self):

        if self.m_head_node.mp_next_node is None:
            return self.m_head_node
        else:
            temp_node = self.m_head_node
            while temp_node.mp_next_node is not None:
                temp_node = temp_node.mp_next_node
            return temp_node

    def add_node(self, node: Node):

        tail_node = self.get_tail_node()
        tail_node.add_next_node(node=node)

    def display(self):

        temp_node = self.m_head_node
        while temp_node.mp_next_node is not None:
            print(str(temp_node.mNode) + "-->", end='')
            temp_node = temp_node.mp_next_node
        print(str(temp_node.mNode) + "-->end", end='')
