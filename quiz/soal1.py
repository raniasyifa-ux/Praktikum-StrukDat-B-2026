"""
Buat fungsi tambah_buku(nama, harga, stok) yang menerima tiga parameter: nama buku (string), harga (int/float), dan stok (int).
2.
Validasi input: harga harus lebih besar dari 0 dan stok tidak boleh bernilai negatif. Jika tidak valid, cetak pesan error dan kembalikan nilai None.
3.
Jika data valid, kembalikan sebuah dictionary dengan key: "nama", "harga", dan "stok".
4.
Di program utama, gunakan perulangan untuk meminta input data 3 buku dari user, simpan ke dalam list, dan tampilkan seluruh isi list di akhir.
5.
Program menampilkan daftar buku yang berhasil ditambahkan beserta seluruh datanya di akhir eksekusi.
"""
katalog = {
    "nama" : [],
    "harga" : [],
    "Stok"  : []
}

def tambah_buku(namaBuku, Harga, Stok):
   namaBuku = []
   Harga = []
   Stok = []

   nama = str(input("Masukkan Nama Buku: "))
   nama.append(namaBuku)

   uang = int(input("Masukkan Harga: "))
   if uang < 0:
      print("HARGA HARUS LEBIH BESAR DARI 0")
      return None
   else:
    uang.append(Harga)

    barang = int(input("Masukkan Stok Barang: "))
    if barang < 0:
      print('error')
      return None
    else:
      barang.append(Stok)
    
    for nama in tambah_buku():
      nama.append(katalog([0]))
    
    for uang in tambah_buku():
      uang.append(katalog([1]))
    
    for barang in tambah_buku():
      barang.append(katalog([2]))


  







    
    