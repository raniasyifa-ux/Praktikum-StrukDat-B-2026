#menetapkan nilai pada properti objek
#menggunakan metode _init_()

class temanku :
    def __init__(self, namanya, umurnya):
        self.namanya = namanya
        self.umurnya = umurnya

teman1 = temanku("Najwa", 19)
print(teman1.namanya, teman1.umurnya)
print(teman1.umurnya)

#jika tanpa menggunakan metode _init_()
class temankulagi :
    pass
teman2 = temankulagi()
teman2.nama = "Farah"
teman2.umur = 20

print(teman2.nama)
print(teman2.umur)

#mengatur nilai default pada _init_()
class temanku :
    def __init__(self, namanya, umurnya = 18):
        self.namanya = namanya
        self.umurnya = umurnya

teman1 = temanku("Najwa", 19)
temandua = temanku('Naurah')
print(teman1.namanya, teman1.umurnya)
print(temandua.namanya, temandua.umurnya)

#kita juga bisa membuat parameter / properti / atribut sebanyak mungkin
class temanku :
    def __init__(self, namanya, umurnya, kelas, akamsi):
        self.namanya = namanya
        self.umurnya = umurnya
        self.kelas = kelas
        self.akamsi = akamsi

teman1 = temanku("Najwa", 19, "TI B", True)
print(teman1.namanya, teman1.umurnya, teman1.kelas, teman1.akamsi)