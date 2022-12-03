from node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def add(self, key, value) -> None:
        node = Node(key, value)
        node.next = self.head
        self.head = node
    
    def remove(self, key) -> None:
        if self.head:
            node = self.head
            if self.head.key == key:
                self.head = self.head.next
            while node.next:
                if node.next.key == key:
                    node.next = node.next.next
                    break
                node = node.next
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        
        return " -> ".join(nodes)