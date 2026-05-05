"""
Sistem daftar buku toko "Literasi"
Toko buku "Literasi" ingin mencatat daftar buku (judul & pengarang)
menggunakan Double Linked List agar bisa ditelusuri dari depan maupun belakang.
1. Buat class Node dengan atribut judul, pengarang, prev, dan next.
2. Buat fungsi insert_tail(), lalu tambahkan buku: Laskar Pelangi, Bumi Manusia,dan Sang Pemimpi.
3. Buat fungsi print_forward() dan print_backward(), lalu jalankan keduanya.
4. Buat fungsi delete_by_judul(), hapus buku "Bumi Manusia", lalu tampilkan list
kembali.

"""

class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.next = None
        self.prev = None
    
def insert_tail(head, judul, pengarang):
        new_node = Node(judul, pengarang)
        if head is None:
            return new_node

        temp = head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

        return head

def print_forward(head):
        temp = head
        while temp:
            print(f'{temp.judul} - {temp.pengarang}')
            temp = temp.next
        print()
    
def print_backward(head):
        if not head:
            return
        
        temp = head
        while temp.next:
            temp = temp.next
        
        while temp:
            print(f'{temp.judul} - {temp.pengarang}')
            temp = temp.prev
        print()
    
def delete_by_judul(head, key):
        temp = head

        while temp:
            if temp.judul == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev
                
                break

            temp = temp.next
        return head
    
jawaban = None
jawaban = insert_tail(jawaban,"Laskar Pelangi", "Andrea Hirata")
jawaban = insert_tail(jawaban,"Bumi Manusia", "Pramoedya Ananta Toer")
jawaban = insert_tail(jawaban,"Sang Pemimpi", "Andrea Hirata")
print("LIST NAMA BUKU DAN PENGARANG SEBELUM DI HAPUS")
print("URUTAN MAJU")
print_forward(jawaban)
print("URUTAN MUNDUR")
print_backward(jawaban)

jawaban = delete_by_judul(jawaban, "Bumi Manusia")
print("LIST BUKU DAN PENGARANG SETELAH DI HAPUS")
print_forward(jawaban)

