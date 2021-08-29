class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
def validateBst(tree):
    # Write your code here.
    return validateBSTHelper(tree, -float('inf'), float('inf'))         

def validateBSTHelper(tree, min, max):
    if tree is None:
        return True
    if tree.value < min or tree.value >= max:
        return False
    leftIsValid = validateBSTHelper(tree.left, min, tree.value)
    
    return leftIsValid and validateBSTHelper(tree.right, tree.value, max)


vali = BST(5)
vali.left = BST(3)
vali.right = BST(7)
vali.left.left = BST(2)
vali.left.right = BST(4)
vali.right.left = BST(6)
vali.right.right = BST(8)

print(validateBst(vali))
