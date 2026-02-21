#properti adalah variabel yang dimiliki suatu kelas.
#membuat kelas dengan properti

class teman:
    def __init__(self, nama, kelas):
        self.nama = nama #properti
        self.kelas = kelas #properti

contoh1 = teman("fildza", "TI B")
print(contoh1.nama + contoh1.kelas) 
#kita mengakses properti suatu objek dengan notasi titik

#mengubah data dari objek
class teman:
    def __init__(self, nama, kelas):
        self.nama = nama #properti
        self.kelas = kelas #properti

contoh1 = teman("fildza", "TI B")
print("ini sebelum diubah ", contoh1.nama + contoh1.kelas) 
contoh1.nama = "Najwa"
print("ini sesudah diubah ", contoh1.nama + contoh1.kelas)

#menghapus properti dari objek
class teman:
    def __init__(self, nama, kelas):
        self.nama = nama #properti
        self.kelas = kelas #properti

contoh1 = teman("fildza", "TI B")

del contoh1.kelas

#properti kelas vs properti objek
class makan :
    spesifikasi = "pedas" #ini adalah properti kelas

    def __init__(self, nama): #ini properti objek
        self.nama = nama

makan1 = makan("pizza")
print(makan1.nama)
print(makan1.spesifikasi)

#memodifikasi properti kelas
class makan :
    spesifikasi = "pedas" #before
    def __init__(self, nama): 
        self.nama = nama

makan1 = makan("pizza")
print(makan1.nama)
print("ini spesifikasi sebelum diubah ", makan1.spesifikasi)

makan1.spesifikasi = "manis" #after
print("ini spesifikasi setelah diubah ", makan1.spesifikasi)

#menambahkan properti baru ke sebuah objek yang sudah ada
class makan :
    spesifikasi = "pedas" #ini adalah properti kelas

    def __init__(self, nama): #ini properti objek
        self.nama = nama

makan1 = makan("pizza")
print(makan1.nama)
print(makan1.spesifikasi)

makan1.ukuran = "jumbo" #menambahkan properti
makan1.banyak = 12 #menambahkan properti

print(makan1.ukuran)
print(makan1.banyak)

