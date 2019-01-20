from BST import BST as bst
from nodeBST import nodeBST as node

bst_tree = bst()
root = node(1)
print(root.get_value())
print(bst_tree.root)
bst_tree.populate_root(root)
print(bst_tree.root.get_value())
node1 = node(-1)
node2 = node(10)
bst_tree.add_node(node1)
bst_tree.add_node(node2)
print(bst_tree.root.left.get_previous().get_value())
print(bst_tree.root.rigth.get_previous().get_value())