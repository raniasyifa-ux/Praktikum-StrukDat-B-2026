class Node:
    def __init__(self, idBuku, Judul):
        self.idBuku = idBuku
        self.Judul = Judul
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def tambah(self, idBuku, Judul):
        def tambahbuku(node, idBuku, Judul):
            if node is None:
             print(f"[INSERT] Berhasil Memasukkan: ID {idBuku} - {Judul}")
             return Node(idBuku, Judul)

            if idBuku < node.idBuku:
              node.left = tambahbuku(node.left, idBuku, Judul)
            elif idBuku > node.idBuku:
               node.right = tambahbuku(node.right, idBuku, Judul)
            return node
        self.root = tambahbuku(self.root, idBuku, Judul)
    
    def Cari(self, idBuku):
       def cariBuku(node, idBuku):
          if node is None:
             return None
          if idBuku == node.idBuku:
             return node
          elif idBuku < node.idBuku:
             return cariBuku(node.left, idBuku)
          elif idBuku > node.idBuku:
             return cariBuku(node.right, idBuku)
       return cariBuku(self.root, idBuku)
    
    def inOrder(self):
       self.no = 1

       def Inorder(node):
            if node is not None:
                Inorder(node.left)
                print(f"{self.no}. {node.idBuku} - {node.Judul}")
                self.no += 1
                Inorder(node.right)

       Inorder(self.root)
    
    def getMin(self):
       node = self.root
       while node and node.left is not None:
          node = node.left
       return node
    
    def getMax(self):
       node = self.root
       while node and node.right is not None:
          node = node.right
       return node
    
    def tinggi(self):
       def Ketinggian(node):
          if node is None:
             return -1
          return 1 + max(Ketinggian(node.left), Ketinggian(node.right))
       return Ketinggian(self.root)


soal = BinarySearchTree()

print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'")
print("============================")

soal.tambah(50, "Dasar Pemprograman")
soal.tambah(30, "Struktur Data")
soal.tambah(70, "Kecerdasan Buatan")
soal.tambah(20, "Matematika Diskrit")
soal.tambah(40, "Basis Data")
soal.tambah(60, "Jaringan Komputer")
soal.tambah(80, "Sistem Operasi")
soal.tambah(90, "Algortima Pemrograman")

print()
print("[INFO] Koleksi Buku (In-Order): ")
soal.inOrder()
print()

cari = 60
hasil = soal.Cari(cari)
print(f"[SEARCH] Mencari ID {cari} .... Ditemukan - Judul: {hasil.Judul}")

carii = 1
hasill = soal.Cari(carii)

if hasill:
   print(f"[SEARCH] Mencari ID {carii} .... Ditemukan - Judul: {hasill.Judul}")
else:
   print(f"[SEARCH] Mencari ID {carii} .... Data Tidak Ditemukan")

kecil = soal.getMin()
besar = soal.getMax()

print("ID TERKECIL: ", kecil.idBuku)
print("ID TERBESAR: ", besar.idBuku)

print("SELESAI \n =========================")

        
