from hash_table import HashTable

hash_table = HashTable()
hash_table.add(123, "Ashok")
hash_table.add(234, "Divakar")
hash_table.add(356, "Dinesh")
hash_table.add(213, "Bindu")

print(hash_table)

print(hash_table.get(213))
print(hash_table.get(123))
print(hash_table.get(234))

hash_table.remove(213)
print("==============After Remove===============")
print(hash_table)