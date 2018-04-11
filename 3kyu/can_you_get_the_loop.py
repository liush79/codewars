class Node(object):
    next = None


def loop_size(node):
    nodes = []
    while True:
        id_node = id(node)
        if id_node in nodes:
            idx = nodes.index(id_node)
            return len(nodes) - idx
        else:
            nodes.append(id_node)
        node = node.next


node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print loop_size(node1)      # 3

