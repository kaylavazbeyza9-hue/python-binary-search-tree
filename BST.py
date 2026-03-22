class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')

def count_nodes(root):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)

def tree_height(root):
    if root is None:
        return 0
    else:
        return max(tree_height(root.left), tree_height(root.right)) + 1

numbers = input("Sıralamak istediğiniz sayıları boşluklarla girin: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

root = None
for num in numbers:
    root = insert(root, num)

print("\nIn-order çıktısı:")
inorder(root)

print("\nPre-order çıktısı:")
preorder(root)

print("\nPost-order çıktısı:")
postorder(root)

print("\nToplam düğüm sayısı:", count_nodes(root))
print("Ağacın yüksekliği:", tree_height(root))