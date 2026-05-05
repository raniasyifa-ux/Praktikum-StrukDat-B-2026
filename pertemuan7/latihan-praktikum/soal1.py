# Gunakan tipe data list bawaan Python.
# 1. Buatlah sebuah list bernama history_array.
# 2. Buat fungsi tambah_pencarian_array(keyword) yang menambahkan kata kunci baru ke
# posisi paling depan (indeks 0).
# o Catatan: Di dalam Array, saat memasukkan data di depan, semua elemen di
# belakangnya harus bergeser.
# 3. Cetak isi history_array.

history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)

tambah_pencarian_array("WEBTOON")

print(history_array)

