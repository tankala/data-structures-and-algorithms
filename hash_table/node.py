class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self) -> str:
        return self.value