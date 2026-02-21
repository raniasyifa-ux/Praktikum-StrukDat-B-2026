"""
buatlah sebuah class dengan
- minimal 3 atribut/properti
- 2 method
lalu buat 3 objek dari class tersbut
lalu ubahlah salah atribut dari obejk tersebut
"""

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
