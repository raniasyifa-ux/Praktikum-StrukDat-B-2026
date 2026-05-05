"""
Sistem antrian kasir toko "Literasi"
Kasir toko menggunakan Circular Linked List untuk antrian pelanggan. Antrian
awal: Andi → Budi → Citra → Dina → (kembali ke Andi).
1. Buat class Node dengan atribut nama dan next. Buat fungsi insert_tail() dan
tambahkan 4 pelanggan.
2. Buat fungsi print_antrian() untuk menampilkan satu putaran antrian.
3. Tambahkan pelanggan baru Edo di akhir antrian menggunakan insert_tail(), lalu
tampilkan antrian.
4. Buat fungsi delete_head(), hapus Andi (sudah dilayani), lalu tampilkan antrian.
"""

class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

def insert_tail(head, nama):
    new_node = Node(nama)

    if head is None:
        new_node.next = new_node
        return new_node
    
    temp = head
    while temp.next != head:
        temp = temp.next

    temp.next = new_node
    new_node.next = head
    return head
def print_antrian(head):
    if head is None:
      return
    
    temp = head
    while True:
        print(f"{temp.nama}")
        temp = temp.next
        if temp == head:
            break
    print()

def delete_head(head, key):
    if head is None:
        return None

    # hanya 1 node
    if head.next == head and head.nama == key:
        return None

    # hapus head
    if head.nama == key:
        last = head
        while last.next != head:
            last = last.next

        head = head.next
        last.next = head
        return head


    temp = head
    while temp.next != head:
        if temp.next.nama == key:
            temp.next = temp.next.next
            break
        temp = temp.next

    return head

jawaban = None

jawaban= insert_tail(jawaban, "Andi")
jawaban= insert_tail(jawaban, "Budi")
jawaban= insert_tail(jawaban, "Citra")
jawaban= insert_tail(jawaban, "Dina")

print("LIST ANTRIAN SEBELUM DI HAPUS: ")
print_antrian(jawaban)

jawaban = insert_tail(jawaban, "Edo")
print("LIST ANTRIAN SETELAH PENAMBAHAN ANGGOTA: ")
print_antrian(jawaban)

jawaban = delete_head(jawaban, "Andi")
print("LIST ANTRIAN YANG TERBARU: ")
print_antrian(jawaban)
