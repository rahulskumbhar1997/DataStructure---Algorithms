from List import List
from Node import Node

if __name__ == "__main__":

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    linked_list = List(node=node_1)
    linked_list.add_node(node=node_2)
    linked_list.add_node(node=node_3)
    linked_list.display()