#contoh list
Nama = ["Rania", "Fildza", "Najwa"]
print(Nama)

#list bisa menduplikasikan data di dalamnya
Nama = ["Rania", "Fildza", "Najwa", "Rania", "Salwa"]
print(Nama)

#list bisa menghitung jumlah index
Nama = ["Rania", "Fildza", "Najwa", "Rania", "Salwa"]
print(len(Nama))

#daftar list
Nama = ["Rania", "Fildza", "Najwa"]
Angka = [4, 11,86, 43, 542]
BOOL = [True, False, False]

#kita bisa memasukkan beda tipe dalam satu list, berbeda dengan array
Gabungan = ["Rania", 18, True, 155, "Female"]

#mengakses item dalam List
NAMA = ["Rania", "Fildza", "Najwa"]
print(NAMA[1])

#pengindeksan negatif
Nama = ["Rania", "Fildza", "Najwa", "Rania", "Salwa"]
print(Nama[-1])

#pengindeksan  menggunakan rentang
Nama = ["Rania", "Fildza", "Najwa", "Rania", "Salwa"]
print(Nama[1:3])

#pengindeksan  menggunakan rentang menghilangkan rentang awal
Nama = ["Rania", "Fildza", "Najwa", "Rania", "Salwa"]
print(Nama[:3])

#pengindeksan  menggunakan rentang menghilangkan rentang akhir
Nama = ["Rania", "Fildza", "Najwa", "Rania", "Salwa"]
print(Nama[2:])

#memanggil fungsi type
mylist = ["INI", "CONTOH", "LIST"]
print(type(mylist))


#Konstruktor list() juga dapat digunakan saat membuat daftar baru
Nama = list(("Rania", "Fildza", "Najwa", "Syifa", 'Farah', 'Salwa', 'Naurah')) # note the double round-brackets
print(Nama)

#Untuk mengubah nilai barang tertentu, lihat nomor indeksnya
contoh1 = ["matematika", "kimia", "fisika"]
contoh1[1] = "pemprograman"
print(contoh1)

#Mengubah Rentang Nilai Item
nama = ["rania", "syifa", "najwa", "salwa", "fildza", "farah"]
nama[1:3] = ["naura", "gledis"]
print(nama)

#Ubah nilai kedua dengan menggantinya dengan dua nilai baru:
nama = ["rania", "syifa", "fildza", 'naura', 'salwa']
nama[1:2] = ["gledis", "farah"]
print(nama)

#Ubah nilai kedua dengan menggantinya dengan satu nilai baru:
nama = ["rania", "syifa", "fildza", 'naura', 'salwa']
nama[1:3] = ["gledis"]
print(nama)

#Insert Items
nama = ["rania", "syifa", "fildza", 'naura', 'salwa']
nama.insert(2, "farah")
print(nama)

#Append Items
nama = ["rania", "syifa", "fildza", 'naura', 'salwa']
nama.append("dimas")
print(nama)


#Extend List
nama1 = ["rania", "syifa", "fildza"]
nama2 = ['naura', 'salwa']
nama1.extend(nama2)
print(nama1)

#Add Any Iterable
thislist = ["rania", "syifa", "fildza"]
thistuple = ('naura', 'salwa')
thislist.extend(thistuple)
print(thislist)

#Remove Specified Item
nama = ["rania", "syifa", "fildza"]
nama.remove("syifa")
print(nama)

#akan menghapus satu 'banana' yang pertama aja
nama = ["rania", "syifa", "fildza",'rania']
nama.remove("rania")
print(nama)

#Remove Specified Index
#The pop() method removes the specified index.
nama = ["rania", "syifa", "fildza",'rania']
nama.pop(1)
print(nama)

#untuk menghapus index terakhir
nama = ["rania", "syifa", "fildza",'rania']
nama.pop()
print(nama)

#Kata kunci tersebut del juga menghapus indeks yang ditentukan:
nama = ["rania", "syifa", "fildza",'rania']
del nama[0]
print(nama)

#Kata kunci tersebut deljuga dapat menghapus daftar sepenuhnya
nama = ["rania", "syifa", "fildza",'rania']
del nama

#Mengosongkan List
nama = ["rania", "syifa", "fildza",'rania']
nama.clear()

"--- loop list ---"
#Loop Through a List
#memanggil setiap index
NAMA = ["RANIA", "SYIFA", "FILDZA", 'NAJWA', 'SALWA']
for x in NAMA:
  print(x)


#Melakukan Perulangan merujuk pada nomor index
NAMA = ["RANIA", "SYIFA", "FILDZA", 'NAJWA', 'SALWA']
for i in range(len(NAMA)):
  print(NAMA[i])

"--- while loop ---"
#Cetak semua item, menggunakan whileperulangan untuk menelusuri semua nomor indeks.
NAMA = ["RANIA", "SYIFA", "FILDZA", 'NAJWA', 'SALWA']
i = 0
while i < len(NAMA):
  print(NAMA[i])
  i = i + 1

#syntax singkat
nama = ["rania", "fildza", "najwa"]
[print(x) for x in nama]


#List Comprehension
"kita akan membuat list baru ketika pada list Nama jika ada huruf r nya"
Nama = ["rania", "fildza", "najwa","salwa",'naura',"farah"]
[print(x) for x in Nama]
newlist = []

for x in Nama:
  if "r" in x:
    newlist.append(x)

print(newlist)

#List Comprehension
Nama = ["rania", "fildza", "najwa","salwa",'naura',"farah"]

newlist = [x for x in Nama if "r" in x]

print(newlist)

"--- Sort List Alphanumerically ---"
"""
Objek List memiliki sort()metode yang akan mengurutkan daftar
secara alfanumerik, menaik, secara default:
"""

Nama = ["rania", "fildza", "najwa","salwa",'naura',"farah"]
Nama.sort()
print(Nama)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Urutkan Menurun
Nama = ["rania", "fildza", "najwa","salwa",'naura',"farah"]
Nama.sort(reverse = True)
print(Nama)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Urutkan daftar berdasarkan seberapa dekat angka tersebut dengan 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Pengurutan berdasarkan huruf besar dan kecil dapat memberikan hasil yang tidak terduga:thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#ekspresi 
"""Ubah nilai-nilai dalam daftar baru menjadi huruf besar"""
newlist = [x.upper() for x in nama]


#mencari item pada suatu List
NAMA = ["RANIA", "SYIFA", "FILDZA", 'NAJWA', 'SALWA']
if "SYIFA" in NAMA:
  print('ADAAAAA')