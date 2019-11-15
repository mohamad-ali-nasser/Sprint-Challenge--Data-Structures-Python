import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")
names_1 = sorted(names_1)  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")
names_2 = sorted(names_2)  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BinarySearchTree('G')
print(len(names_1[1:]))
n=0
# for i in names_1[n:]:
#     print(i)
#     bst.insert(i)
#     n+=1
#     print(n)
#     # print(bst.left.right.value)
# print(bst.right.value)

# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)






end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

