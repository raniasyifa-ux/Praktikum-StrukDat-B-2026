#self sangat penting karena digunakan untuk mengakses properdi yang ada di dalam kelas
class makanan:
    def __init__(self, namaMakanan): 
        self.namaMakanan = namaMakanan 
    
    def tampil(self):
        print("makanan kamu " + self.namaMakanan)

makan = makanan("pizza")
makan.tampil()

#kita juga bisa mengganti self dengan nama yang kita mau
#contohnya mengganti self dengan nakMakan
class makanan:
    def __init__(nakMakan, namaMakanan):
        nakMakan.namaMakanan = namaMakanan
    
    def tampil(nakMakan):
        print("makanan kamu " + nakMakan.namaMakanan)

makan = makanan("Mie Ayam")
makan.tampil()

#kita juga bisa memanggil method di dalam method menggunakan self
class minuman:
    def __init__(self, namaMinum):
        self.namaMinum = namaMinum
    
    def tampil(self):
        return "Nama Minumanmu " + self.namaMinum
    
    def pesan(self):
        kata = self.tampil()
        print(kata + ", Abisin")

minum = minuman("Jus")
minum.pesan()