class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def Tambah_Root(self, data):
        self.root = Node(data)
    
    def Tambah_Kiri(self, parent, data):
        if parent.left is None:
            parent.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent.left
            parent.left = new_node
    
    def Tambah_Kanan(self, parent, data):
        if parent.right is None:
            parent.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent.right
            parent.right = new_node
    

class binarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data): #LANGKAH 1
        new = Node(data)

        #jika tidak ada root # LANGKAH 2
        if self.root == None:
            self.root = new
            return
        
        #jika ada root LANGKAH 3
        p = self.root
        q = self.root

        #LANGKAH 4
        while q != None and new.data != p.data:
            p = q #LANGKAH 5

            #LANGKAH 6
            if new.data < p.data:
                q = p.left
            else: #jika tidak 
                q = p.right

            #LANGKAH 7
        if new.data == p.data:
            print("SAMAA")
            return
            
        #LANGKAH 8
        #jika tidak new.data == p.data
        if new.data < p.data:
            p.left = new
        else:
            p.right = new    

        
        #LANGKAH 9 SELESAI


bst = binarySearchTree()
bst.insert(13)
bst.insert(34)
bst.insert(14)
bst.insert(21)
bst.insert(62)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

inorder(bst.root)

soal = BinaryTree()

soal.Tambah_Root("F")
soal.Tambah_Kiri(soal.root, "B")
soal.Tambah_Kanan(soal.root, "G")

soal.Tambah_Kiri(soal.root.left, "A")

soal.Tambah_Kiri(soal.root.right, "D")
soal.Tambah_Kanan(soal.root.right, "I")

soal.Tambah_Kiri(soal.root.right.left, "C")
soal.Tambah_Kanan(soal.root.right.left, "E")

soal.Tambah_Kiri(soal.root.right.right, "H")

print()
inorder(soal.root)