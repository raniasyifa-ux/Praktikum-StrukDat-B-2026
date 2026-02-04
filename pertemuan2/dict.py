thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary Items
#Cetak nilai "merek" dari kamus tersebut:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Nilai duplikat akan menimpa nilai yang sudah ada:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # yang akan di print year = 2020

#Dictionary Length
#Untuk menentukan berapa banyak item yang dimiliki kamus, gunakan fungsi: len()

#Cetak jumlah item dalam kamus:
print(len(thisdict))

#tipe data

#Tipe data string, int, boolean, dan list:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#tipe()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#Konstruktor dict()
#Konstruktor dict() juga dapat digunakan untuk membuat dict()
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
