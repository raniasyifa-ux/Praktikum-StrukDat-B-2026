#list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#list bisa menduplikasikan data di dalamnya
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#list bisa menghitung jumlah index
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#daftar list
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#kita bisa memasukkan beda tipe dalam satu list, berbeda dengan array
list1 = ["abc", 34, True, 40, "male"]

#memanggil fungsi type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Konstruktor list() juga dapat digunakan saat membuat daftar baru
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Untuk mengubah nilai barang tertentu, lihat nomor indeksnya
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Mengubah Rentang Nilai Item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Ubah nilai kedua dengan menggantinya dengan dua nilai baru:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#akan menghapus satu 'banana' yang pertama aja
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#untuk menghapus index terakhir
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Kata kunci tersebut del juga menghapus indeks yang ditentukan:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Kata kunci tersebut deljuga dapat menghapus daftar sepenuhnya
thislist = ["apple", "banana", "cherry"]
del thislist

"--- loop list ---"
#Loop Through a List
#memanggil setiap index
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

"--- while loop ---"
#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#syntax singkat
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#List Comprehension
"kita akan membuat list baru ketika pada list fruits jika ada huruf a nya"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

"--- Sort List Alphanumerically ---"
"""
Objek List memiliki sort()metode yang akan mengurutkan daftar
secara alfanumerik, menaik, secara default:
"""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Urutkan Menurun
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

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
