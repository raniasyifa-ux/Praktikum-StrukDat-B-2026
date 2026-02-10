#tuple
Nama = ("rania", "fildza", "najwa")
print(Nama)


#izin duplikat
Nama = ("rania", "fildza", "najwa",'fildza')
print(Nama)


#mencari panjang tuple
Nama = ("rania", "fildza", "najwa",'fildza')
print(len(Nama))

#tuple dengan satu item, memakai tanda koma dibelakang
Nama = ("rania",)
print(type(Nama))

contoh1 = ("rania", "fildza", "najwa",'fildza')
contoh2 = (44,68,65,-8,9)
contoh3 = (True, False, False)

print(contoh1)
print(contoh2)
print(contoh3)

#mengetahui class tipe data tuple
Nama= ("rania",)
print(type(Nama))

#konstruktor tuple
NAma = tuple(("rania", "fildza", "salwa"))
print(NAma)


#mengakses tuple
NAma = tuple(("rania", "fildza", "salwa"))
print(NAma[1])

#mengakses dimulai dari index terakhir (negatif index)
NAma = tuple(("rania", "fildza", "salwa"))
print(NAma[-1])

#mengakses dengan menentukan index pertama dan terakhir
NAma = tuple(("rania", "fildza", "salwa", 'najwa', 'farah', 'syifa'))
print(NAma[0:3])

#mengakses dengan hanya menentukan index terakhir
NAma = tuple(("rania", "fildza", "salwa", 'najwa', 'farah', 'syifa'))
print(NAma[:2])

#mengakses dengan hanya menentukan index awal
NAma = tuple(("rania", "fildza", "salwa", 'najwa', 'farah', 'syifa'))
print(NAma[2:])

#mengakses dengan hanya menentukan index awal dan akhir menggunakan indeks negatif
NAma = tuple(("rania", "fildza", "salwa", 'najwa', 'farah', 'syifa'))
print(NAma[-3:-1])

#memeriksa item dalam tuple
contoh1 = ("rania", "fildza", "najwa",'fildza')
if "fildza" in contoh1:
    print("ada nama fildza")



#mengubah tuple menjadi list, mengganti item, konversi kembali menjadi tuple
contoh1 = ("rania", "fildza", "najwa",'fildza')
y = list(contoh1)
y[1] = "salwa"
contoh1 = tuple(y)

print(contoh1)

#konversi menjadi daftar
contoh1 = ("rania", "fildza", "najwa",'fildza')
nama = list(contoh1)
nama.append("syifa")
thistuple = tuple(nama)

#menambah tuple ke tuple
nama = ("rania", "syifa", "fildza", 'najwa', 'salwa')
y = ("naurah",)
nama += y

print(nama)


#menghapus item dengan mengubahnya terlebih dahulu menjadi List, lalu konversi kembali
contoh1 = ("rania", "fildza", "najwa",'fildza')
y = list(contoh1)
y.remove("najwa",)
contoh1 = tuple(y)
print(contoh1)

#menghapus tuple sepenuhnya
nama =("rania", "fildza", "najwa",'fildza')
del nama

#packing tuple
nama =("rania", "fildza", "najwa",'fildza')

#unpacking tuple
nama =("rania", "fildza", "najwa",'salwa')

(satu,dua,tiga,empat) = nama

print(satu)
print(dua)
print(tiga)
print(empat)

#penggunaan arsentik *
nama =("rania", "fildza", "najwa",'salwa','naurah','farah')

(satu,dua,*tiga) = nama

print(satu)
print(dua)
print(tiga)

#penggunaan arsentik di tengah variabel
nama =("rania", "fildza", "najwa",'salwa','naurah','farah')

(satu,*dua,tiga) = nama

print(satu)
print(dua)
print(tiga)

print('PERULANGAN')
#perulangan pada tuple
nama =("rania", "fildza", "najwa",'salwa','naurah','farah')
for x in nama:
  print(x)

#melakukan perulangan melalui item tuple dengan merujuk pada nomor indeksnya.
nama =("rania", "fildza", "najwa",'salwa','naurah','farah')
for i in range(len(nama)):
  print(nama[i])

#menggunakan while loop
nama =("rania", "fildza", "najwa",'salwa','naurah','farah')
i = 0
while i < len(nama):
  print(nama[i])
  i = i + 1


#menggabungkan dua tuple
contoh4 = ("contoh1", "contoh2" , "contoh3")
contoh5 = (22, 42, 11)

contoh6 = contoh4 + contoh5
print(contoh6)

#melakukan perkalian kepada item dalam tuple
contoh4 = ("contoh1", "contoh2" , "contoh3")
contoh7 = (contoh4 * 2)
print(contoh7)

