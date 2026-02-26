"""
Diberikan data buku dalam bentuk dictionary:
transaksi = [
{"produk": "Buku", "harga": 10000, "jumlah": 3},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]
a.
Ubah jumlah buku menjadi 8.
b.
Tambahkan 2 produk baru.
c.
Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan perulangan.
Tampilkan ringkasan seperti ini:
Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.
"""

transaksi = [
{"produk": "Buku", "harga": 10000, "jumlah": 3},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

#a
transaksi[0]["jumlah"] = 8
print(transaksi)

#b
transaksi.append({"produk": "kertas", "harga": 12000, "jumlah": 7})
transaksi.append({"produk": "tip x", "harga": 23000, "jumlah": 6})
print(transaksi)

#c
transaksi= [
{"produk": "Buku", "harga": 10000, "jumlah": 8},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 26000, "jumlah": 23},
{"produk": "kertas", "harga": 12000, "jumlah": 7},
{"produk": "tip x", "harga": 23000, "jumlah": 6}
]
jumlah = 0
harga = 0

for x in transaksi:
    
    total = (x["jumlah"] * x["harga"])
    print(f"{x["produk"]} | Total: {total}")
