from node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def add(self, data) -> None:
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def remove(self) -> None:
        node = self.head
        if node is not None:
            self.head = node.next
            node.next = None
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        return " -> ".join(nodes)