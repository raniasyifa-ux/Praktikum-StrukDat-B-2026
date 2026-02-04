"""
1. Diberikan sebuah list angka:
angka = [10, 20, 30, 40, 50]
1. Tambahkan angka 60 ke dalam list.
2. Hapus angka 20 dari list.
3. Tampilkan angka tertinggi dan terendah
4. Hitung rata-rata angka setelah perubahan data
5. Tampilkan seluruh isi list setelah perubahan.
"""
#1. tambahkan angka 60
angka = [10, 20, 30, 40, 50] 
angka.append(60)
print(angka)
#2. menghapus angka 20
angka.remove(20)
angka.sort(reverse=True)

print(angka)
#3. menghitung rata rata
total = 0
jumlah = 0
for x in angka :
    total += x
    jumlah += 1
    rata = total / jumlah

print("rata rata nya adalah ", rata)



