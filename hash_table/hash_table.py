from linked_list import LinkedList

class HashTable:

    def __init__(self) -> None:
        self.HASH_TABLE_ARRAY_SIZE = 10
        self.array = [LinkedList() for index in range(self.HASH_TABLE_ARRAY_SIZE)]
    
    def get_hash(self, key):
        return key % self.HASH_TABLE_ARRAY_SIZE
    
    def add(self, key, value) -> None:
        hash = self.get_hash(key)
        linked_list = self.array[hash]
        linked_list.add(key, value)
    
    def get(self, key):
        hash = self.get_hash(key)
        linked_list = self.array[hash]
        node = linked_list.head
        while node:
            if node.key == key:
                return node.value
            node = node.next
    
    def remove(self, key):
        hash = self.get_hash(key)
        linked_list = self.array[hash]
        linked_list.remove(key)
    
    def __repr__(self) -> str:
        data_in_hashmap = []
        for element in self.array:
            if str(element):
                data_in_hashmap.append(str(element))
        
        return ", ".join(data_in_hashmap)