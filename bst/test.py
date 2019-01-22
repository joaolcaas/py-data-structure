from BST import BST as bst 

bst_tree = bst()

bst_tree.add_node(2)
print(bst_tree.root)
bst_tree.add_node(-1)
bst_tree.add_node(-2)
bst_tree.add_node(-3)
print(bst_tree.root.get_left().get_value())
bst_tree.delete_node(-1)
print(bst_tree.root.get_left().get_value())
#print(bst_tree.root)
print(bst_tree.is_empty())