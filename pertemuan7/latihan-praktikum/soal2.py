# Tugas 2: Implementasi Menggunakan Singly LinkedList
# Buatlah struktur manual menggunakan Class.
# 1. Buat class Node dan class HistoryLinkedList.
# 2. Buat metode tambah_pencarian_linked(keyword) yang menambahkan node baru di posisi
# Head.
# o Catatan: Di LinkedList, Anda hanya perlu mengubah pointer next node baru ke head
# lama.
# 3. Buat metode tampilkan_history() untuk mencetak riwayat.

class Node:
    def __init__(self, keyword):
        self.keyword = keyword
        self.next = None
    
class HistoryLinkedList :
    def __init__(self):
        self.head = None
    
    def tambah_pencarian_linked (self, keyword):
        NewNode = Node(keyword)
        NewNode.next = self.head
        self.head = NewNode
    

    def tampilkan_history(self):
        currentNode = self.head

        while currentNode:
         print(currentNode.keyword, end=" -> ")
         currentNode = currentNode.next
        print("null")

pemanggilan = HistoryLinkedList()
pemanggilan.tambah_pencarian_linked("WEBTOON")
pemanggilan.tambah_pencarian_linked("google.com")
pemanggilan.tambah_pencarian_linked("python.org")
pemanggilan.tampilkan_history()



