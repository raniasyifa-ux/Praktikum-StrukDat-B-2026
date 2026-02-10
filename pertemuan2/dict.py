nama = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007
}

print(nama)

#tidak menampilkan nilai duplikat
nama = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "tahun" : 2026
}
print(nama)

#menghitung panjang dict
print(len(nama))

#item dalam dict dapat berupa tipe data yang berbeda
nama = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "tahun" : 2026,
  "hasil" : True
}
print(nama)

#mengetahui class dari dict
contoh = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "tahun" : 2026,
  "hasil" : True
}

print(type(contoh))

#konstruktor dict
thisdict = dict(name = "rania", age = 19, country = "Indonesia")
print(thisdict)

#mengakses dict melalui key
contoh = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "tahun" : 2026,
  "hasil" : True
}
x = contoh["hasil"]
print(x)

#menggunakan fungsi get()
x = contoh.get("tahun")

#mendapatkan daftar kunci
y = contoh.keys()
print(y)

#mendapatkan daftar nilai
y = contoh.values()
print(y)

#mendapatkan daftar 
y =contoh.items()
print(y)

#memeriksa apakah item ada pada dict
contoh = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "tahun" : 2026,
  "hasil" : True
}
if "umur" in contoh:
    print("done")

#mengubah item dengan merujuk kunci
contoh = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "hasil" : True
}

contoh["umur"] = 20
print(contoh)

#mengubah item menggunakan fungsi update
contoh = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "hasil" : True
}
contoh.update({"nama": 'fildza'})
print(contoh)

#menambahkan nilai baru
contoh = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "hasil" : True
}
contoh["matkul"] = "Struktur Data"
print(contoh)

#menghapus item
contoh.pop("matkul")
print(contoh)

#menghapus item terakhir
contoh.popitem()
print(contoh)

#menggunakan kata kunci del
del contoh["tahun"]
print(contoh)

#menggunakan fungsi clear() untuk mengahpus dict
contoh.clear()
print(contoh)

#melakukan perulangan for (menampilkan kunci)
contoh = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "hasil" : True
}

for x in contoh:
    print(x)

#melakukan perulangan for (menampilkan nilai)
contoh = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "hasil" : True
}

for x in contoh:
    print(contoh[x])


#menggunakan values()
for x in contoh.values():
    print(x)

#menggunakan keys()
for x in contoh.keys():
    print(x)

#menggunakan items() untuk perulangan keys  dan values
for x, y in contoh.items():
    print(x,y)

#copy dict
contoh = {
  "nama": "rania",
  "umur": "19",
  "tahun": 2007,
  "hasil" : True
}
copyannya = contoh.copy()
print(copyannya)

#copy dengan menggunakan dict()
copylagi = dict(contoh)
print(copylagi)

#MEMBUAT DICT DI DALAM DICT
temantemanku = {
  "pertama" : {
    "name" : "fildza",
    "year" : 2006
  },
  "kedua" : {
    "name" : "najwa",
    "year" : 2006
  },
  "ketiga" : {
    "name" : "syifa",
    "year" : 2007
  }
}
print(temantemanku)

#menggabungkan dict
pertama = {
  "name" : "fildza",
  "year" : 2006
}
kedua = {
  "name" : "najwa",
  "year" : 2007
}
ketiga = {
  "name" : "syifa",
  "year" : 2006
}

temanku = {
  "pertama" : pertama,
  "kedua" : kedua,
  "ketiga" : ketiga
}
print(temanku)

#menampilkan satu item dalam dict

print(temanku["kedua"]["name"])

#perulangan melalui kunci dan nilai dalam nested dict
for x, obj in temanku.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])