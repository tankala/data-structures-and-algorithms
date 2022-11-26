class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None
    
    def __repr__(self) -> str:
        return self.data