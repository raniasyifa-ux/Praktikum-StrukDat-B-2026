# Gunakan class Node dan AntreanLinkedList.
# 1. Implementasikan fungsi insert_at_position(head, nama_pasien, posisi) seperti kode yang
# kamu punya sebelumnya (menggunakan logika position - 2).
# 2. Tugas Tambahan: Tambahkan validasi sederhana. Jika posisi yang dimasukkan lebih besar
# dari jumlah pasien yang ada, maka pasien tersebut otomatis diletakkan di paling akhir
# (Append).

class Node :
    def __init__(self, namaPasien):
        self.namaPasien = namaPasien
        self.next = None

class AntreanLinkedList:
    def __init__(self):
        self.head = None
    
    def Tambah(self, nama_pasien):
        nodeBaru = Node(nama_pasien)

        if not self.head:
            self.head = nodeBaru
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = nodeBaru

    def insert_at_position(self, nama_pasien, posisi):
        nodeBaru = Node(nama_pasien)

        if posisi == 1 or not self.head :
            nodeBaru.next = self.head
            self.head = nodeBaru
            return
        
        current = self.head
        counter = 1

        while current.next and counter < posisi - 1:
            current = current.next
            counter += 1

        
        nodeBaru.next = current.next
        current.next = nodeBaru
    
    def menampilkan (self):
        current = self.head

        while current:
            print(current.namaPasien, end=",")
            current = current.next
        print('None')


jawaban = AntreanLinkedList()
jawaban.Tambah('PASIEN A (STABIL)')
jawaban.Tambah('PASIEN B (STABIL)')
jawaban.Tambah('PASIEN C (STABIL)')

jawaban.insert_at_position('PASIEN D (DARURAT)', 2)

jawaban.menampilkan()