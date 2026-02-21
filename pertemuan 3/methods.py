#contoh method
class teman:
    def __init__(self, nama, umur): #ini method
        self.nama = nama
        self.umur = umur
    
    def tampil(self):
        print(f"nama temanku {self.nama}, dan umurnya {self.umur}")

teman1 = teman("fildza", 19)
teman1.tampil()

#method dengan parameter
class perhitungan:
    def tambah(self,a, b):
        return a + b
    
    def pengurangan(self, a, b):
        return a - b
kalkulator = perhitungan()
print(kalkulator.tambah(4,6))
print(kalkulator.pengurangan(5,3))

#method yang mengakses properti objek
class teman:
    def __init__(self, nama, umur): 
        self.nama = nama
        self.umur = umur
    
    def tampil(self):
        print(f"nama temanku {self.nama}, dan umurnya {self.umur}")

teman1 = teman("fildza", 19)
teman1.tampil()

#method yang memodifikasi nilai properti
class teman:
    def __init__(self, nama, umur): #ini method
        self.nama = nama
        self.umur = umur
    
    def tampil(self):
        print(f"nama temanku {self.nama}, dan umurnya {self.umur}")
    
    def ultah(self):
        self.umur += 1
        print(f"tahun ini, dia berumur {self.umur}")
teman1 = teman("fildza", 19)
teman1.tampil()
teman1.ultah()

#method tanpa_str_()
class teman:
    def __init__(self, nama, umur): #ini method
        self.nama = nama
        self.umur = umur
    
    def tampil(self):
        print(f"nama temanku {self.nama}, dan umurnya {self.umur}")

teman1 = teman("fildza", 19)
teman1.tampil()

#method menggunakan _str_()
class teman:
    def __init__(self, nama, umur): #ini method
        self.nama = nama
        self.umur = umur
    
    def __str__(self):
        return f"nama temanku {self.nama}, dan umurnya {self.umur}"

teman1 = teman("najwa", 19)
print(teman1)

#class memungkinkan mempunyai lebih dari dua mtehos yang saling bekerja sama
class Makanan:
    def __init__(self,namaMakan, JumlahMakan, kategori ):
        self.namaMakan = namaMakan
        self.jumlah =JumlahMakan
        self.kategori = kategori  
    
    def maumakan(self, namaMakan):
        print(f"aku mau makan {namaMakan}")
    
    def jumlah(self):
        print("jumlah makanan: ")
    
    def ubah_jumlah(self, jumlahBaru):
        self.jumlah = jumlahBaru
    

a1 = Makanan("pizza", 7, "enak")
a2 = Makanan("mie", 6, "pedas")
a3 = Makanan("dimsum", 9, "berdaging")

a2.maumakan("pizza")

print(f"jumlah sebelum diubah {a3.jumlah}")
a3.ubah_jumlah(30)
print(f"sekarang jumlahnya {a3.jumlah} ")

#menghapus method dalam class

class teman:
    def __init__(self, nama, umur): #ini method
        self.nama = nama
        self.umur = umur
    
    def __str__(self):
        return f"nama temanku {self.nama}, dan umurnya {self.umur}"

teman1 = teman("najwa", 19)
print(teman1)

del teman.__str__
