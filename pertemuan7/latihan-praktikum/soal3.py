# Gunakan list bawaan Python antrean_array.
# 1. Buat list antrean_array dengan data awal di atas.
# 2. Buat fungsi sisipkan_pasien_darurat_array(nama_pasien, posisi):
# o Gunakan metode .insert(posisi - 1, nama_pasien).
# o Analisis: Apa yang terjadi pada pasien di belakangnya saat pasien baru masuk di
# tengah?
# 3. Cetak antrean akhir.

antrean_array = [
    "PASIAN A (STABIL)",
    "PASIAN B (STABIL)",
    "PASIAN C (STABIL)"
]

def sisipkan(namaPasien, Nomor):
    antrean_array.insert(Nomor - 1, namaPasien)

sisipkan("PASIEN D (DARURAT)", 2)

for i in antrean_array:
    print(i)

#ANALISIS
'''
yang akan terjadi pada pasian di belakangnya adalah, antriannya akan bergeser, atau mundur 1 kebelakang, jadi 
yang awalnya A - B - C 
menjadi A - D - B - C
'''