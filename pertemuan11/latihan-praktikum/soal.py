class Node:
  def __init__(self, nama, keluhan):
    self.nama = nama
    self.keluhan = keluhan
    self.next = None

class RumahSakit:
  def __init__(self):
    self.head = None
    self.tail = None
    self.sizee = 0

  def enqueue(self, nama, keluhan):
    new_node = Node(nama, keluhan)
    if self.tail is None:
      self.head = self.tail = new_node
      self.sizee += 1
      return
    self.tail.next = new_node
    self.tail = new_node
    self.sizee += 1

  def dequeue(self):
    if self.isEmpty():
      return "Pasien tidak ada"
    temp = self.head
    self.head = temp.next
    self.sizee -= 1
    if self.head is None:
      self.tail = None
    return temp.nama

  def peek(self):
    if self.isEmpty():
      return "ANTRIAN KOSONG"
    return self.head.nama

  def isEmpty(self):
    return self.sizee == 0

  def size(self):
    return self.sizee
  
  def clear(self):
    self.head = None
    self.tail = None
    self.sizee = 0

  def printQueue(self):
    temp = self.head
    antrian = 1
    while temp:
      print('[DAFTAR]',temp.nama,'Terdaftar dengan keluhan', temp.keluhan, end="\n")
      temp = temp.next
      print(f"Nomor Antrian = {antrian}")
      antrian += 1
    print()

  
print("==========")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("==========")

DataPasien = RumahSakit()
print("[CEK] Apakah antrian kosong?  ", DataPasien.isEmpty())
print()

DataPasien.enqueue('Budi', 'Demam Tinggi')
DataPasien.enqueue('Ani', "Batuk Pilek")
DataPasien.enqueue('Citra', "Sakit Kepala")


DataPasien.printQueue()

print("[INFO] jumlah pasien yang menunggu: ", DataPasien.sizee)
print()
print("[PEEK] Pasien yang akan dipanggil: ", DataPasien.peek())
print()
print("[PANGGIL] Pasien yang dipanggil oleh dokter: ", DataPasien.dequeue())
print()
DataPasien.enqueue('Dodi', "Nyeri Perut")

print("[ANTRIAN SAAT INI]")
DataPasien.printQueue()


print("[[INFO] Pasien yang dipanggil oleh dokter: ", DataPasien.dequeue())
print()

print("[PANGGIL] Jumlah Pasien Saat ini: ", DataPasien.sizee)
print()

print("[CLEAR] Mengkosongkan Antrian: ", DataPasien.clear())
print()
print("[CEK] Apakah antrian kosong?  ", DataPasien.isEmpty())
print()