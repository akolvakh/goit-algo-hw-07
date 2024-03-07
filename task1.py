class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def min_node(node):
    current = node
    while current.left:
        current = current.left
    return current.val

def max_node(node):
    current = node
    while current.right:
        current = current.right
    return current.val

def sum_of_nodes(node):
    total = node.val
    if node.left is not None:
        total += sum_of_nodes(node.left)
    if node.right is not None:
        total += sum_of_nodes(node.right)
    return total

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def delete(root, key):
    if not root:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_node(root.right)
        root.right = delete(root.right, root.val)
    return root

root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

print(root)

print("Мінімум:", min_node(root))
print("Максимум", max_node(root))
print("Сума:", sum_of_nodes(root))
