myset = {"apple", "banana", "cherry"}

#Item yang sudah ditetapkan tidak dapat diubah, tetapi Anda dapat menghapus item dan menambahkan item baru.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplikat Tidak Diizinkan
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#True dan 1 dianggap memiliki nilai yang sama:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#ilai False dan 0 dianggap sebagai nilai yang sama dalam himpunan, dan diperlakukan sebagai duplikat:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Menghitung Panjang Satu Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Set Item - Tipe Data
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

#tipe()
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Konstruktor set()
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#menambahkan item
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Tambahkan elemen dari tropicalke dalam thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Tambahkan Objek Iterasi Apa Pun
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# Remove Set Items
#kalau pakai remove, akan error kalau ga ada di list
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#memakai discard, kalau pakai ini ndk error kalau ndk da itemnya
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#The return value of the pop() method is the removed item.
#Himpunan tidak berurutan , jadi saat menggunakan pop()metode ini,
# Anda tidak tahu item mana yang akan dihapus.
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
