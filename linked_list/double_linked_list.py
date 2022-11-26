from node_double import Node

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def add(self, data) -> None:
        node = Node(data)
        current_head = self.head
        node.next = current_head
        if current_head is not None:
            current_head.previous = node
        self.head = node
    
    def remove(self) -> None:
        node = self.head
        if node is not None:
            self.head = node.next
            self.head.previous = None
            node.next = None
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        return " <-> ".join(nodes)