from BST import BST as bst 

bst_tree = bst()
print(bst_tree.root)
bst_tree.populate_root(1)
print(bst_tree.root.get_value())
bst_tree.add_node(-1)
bst_tree.add_node(10)
print(bst_tree.root.left.get_previous().get_value())
print(bst_tree.root.rigth.get_previous().get_value())
print(bst_tree.root.left.get_value())