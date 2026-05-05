class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def InsertManual (self):
        root1 = Node("A")
        node2 = Node("B")
        node3 = Node("C")
        node4 = Node("D")
        node5 = Node("E")
        node6 = Node("F")
    
        self.root = root1
        root1.left = node2
        root1.right = node3
        node2.left = node4
        node2.right = node5
        node3.right = node6

    def preorder(self, node):
        if node is not None:
            print(node.data, end="->")
            self.preorder(node.left)
            self.preorder(node.right)
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end="->")
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end="->")

    def getLeafNodes(self, node, leaf):
        if node is not None:
            if node.left is None and node.right is None:
                leaf.append(node.data)
            self.getLeafNodes(node.left, leaf)
            self.getLeafNodes(node.right, leaf)


soal = BinaryTree()
soal.InsertManual()

print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI' ")
print("=====================================")

print()

print("[INFO] Membangun Struktur Gudang...")
print()
print("[INFO] Struktur berhasil dibuat.")

print()
print("HASIL AUDIT: ")

print()
print("1. Pre-Order : ")
soal.preorder(soal.root)
print()

print("2. In-Order: ")
soal.inorder(soal.root)
print()

print("3. Post - Order: ")
soal.postorder(soal.root)
print()

jawaban = []
soal.getLeafNodes(soal.root, jawaban)
print("[DATA] Gudang Ujungnya: ", ', '.join(jawaban))
print()
print("====================================")
print("AUDIT SELESAI")