

#Item yang sudah ditetapkan tidak dapat diubah, tetapi Anda dapat menghapus item dan menambahkan item baru.
nama = {"rania", "syifa", "najwa", 'fildza'}
print(nama)


#Duplikat Tidak Diizinkan
nama = {"rania", "syifa", "najwa", 'fildza'}
print(nama)


#True dan 1 dianggap memiliki nilai yang sama:
nama = {"rania", "syifa", "najwa", 'fildza', True, 1, 2}
print(nama)

#Nilai False dan 0 dianggap sebagai nilai yang sama dalam himpunan, dan diperlakukan sebagai duplikat:
nama = {"rania", "syifa", "najwa", 'fildza', False, True, 0}

print(nama)

#Menghitung Panjang Satu Set
nama = {"rania", "syifa", "najwa", 'fildza'}

print(len(nama))

#Set bisa berisi oleh satu item, tetapi harus ada koma setelah item agar Set terbaca sebagai tipe data Set.
nama = {"rania", }
print(type(nama))



#Set Item - Tipe Data
nama = {"rania", "syifa", "najwa", 'fildza'}
angka = {1, 5, 7, 9, 3}
boolean = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

#tipe()
myset = {"rania", "syifa", "najwa", 'fildza'}
print(type(myset))

#Konstruktor set()
nama = set(("rania", "syifa", "najwa", 'fildza')) 
print(nama)

#mencari item dalam Set
nama = {"rania", "syifa", "najwa", 'fildza'}
for x in nama:
  print(x)

#menambahkan item
nama = {"rania", "syifa", "najwa", 'fildza'}
nama.add("farah")
print(nama)

#Tambahkan elemen dari tropicalke dalam thisset:
nama = {"rania", "syifa", "najwa", 'fildza'}
angka = {"12", "211", "677"}

nama.update(angka)
print(nama)

#Tambahkan Objek Iterasi Apa Pun
nama = {"rania", "syifa", "najwa", 'fildza'}
mylist = ["farah", "naurah"]

nama.update(mylist)
print(nama)

# Remove Set Items
#kalau pakai remove, akan error kalau ga ada di list
namabuah = {"mangga", "pisang", "kiwi"}
namabuah.remove("pisang")

print(namabuah)


#memakai discard, kalau pakai ini ndk error kalau ndk da itemnya
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#The return value of the pop() method is the removed item.
#Himpunan tidak berurutan , jadi saat menggunakan pop()metode ini,
# Anda tidak tahu item mana yang akan dihapus.
nama = {"rania", "syifa", "najwa", 'fildza'}
x = nama.pop()

print(x)
print(nama)

#fungsi clear
nama = {"rania", "syifa", "najwa", 'fildza'}
nama.clear()
print(nama)

#menggunakan kata kunci del untuk menghapus seluruh Set
nama = {"rania", "syifa", "najwa", 'fildza'}
del nama

#menggabungkan dua set atau lebih
nama = {"rania", "syifa", "najwa", 'fildza'}
angka = {"12", "211", "677"}

gabungan = nama.union(angka)
print(gabungan)

#pengganti union()
gabungan = nama | angka
print(gabungan)

#menggabungkan Set dengan tipe data lain
nama = ('rania', 'fildza')
nama2 = {"farah",'naurah'}

gabung = nama2.union(nama)
print(gabung)

#menampilkan kata yang duplikat
nama = {'rania', 'fildza','najwa','salwa'}
nama2 = {"farah",'naurah','rania'}

contoh = nama.intersection(nama2)
print(contoh)

#pengganti fungsi intersection
contoh1 = nama&nama2
print(contoh1)

#mengubah himpunan asli alih-alih mengembalikan himpunan baru.
nama.intersection_update(nama2)
print(nama)