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
    
    def remove_kth_node_from_end(self, k):
        slow = self.head
        fast = self.head

        while k > 0:
            if fast:
                fast = fast.next
                k -= 1
            else:
                print("Wrong K")
                return
        
        if fast:
            while fast.next:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
        else:
            self.head = self.head.next
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        return " -> ".join(nodes)