from linked_list import LinkedList

linked_list = LinkedList()

linked_list.add("5")
linked_list.add("4")
linked_list.add("3")
linked_list.add("2")
linked_list.add("1")

print(linked_list)

linked_list.remove_kth_node_from_end(4)
print("----------------After Remove-------------------")
print(linked_list)