
#DATA AWAL YANG TERSEDIA
pasien_hari_ini = [ 
                    {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False},
                    {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True}, 
                    {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False}, 
                    {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True}, {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False}, 
                    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False},]

#SOAL 1. MEMBUAT LIST DAN DICTIONARY

def tampilkan_pasien(): #membuat fungsi bernama tampilkan_pasien untuk menampilkan pasien pasien yang ada 
    print("=== DATA PASIEN KLINIK ===") #membbuat header/judul untuk tabel
    print("No | ID | Nama | Usia | Penyakit | Status Bayar") #membuat judul untuk setiap kolom
    nomor = 0
    for i in pasien_hari_ini: #menggunakan perulangan, untuk setiap i di dalam  range dictionary pasien_hari_ini
        print(f"{nomor+1} | {i['id']} | {i["nama"]} | {i["usia"]} | {i["penyakit"]} | {i["bayar"]}") #menampilkan data setiap pasien 
        nomor+=1
    return #kembalikan

def filter_belum_bayar(): #membuat fungsi mendata pasien yang belum bayar
    yang_belum_bayar = [] #membbuat list kosong

    
    if pasien_hari_ini["Bayar"] == False: #menggunakan pemilihan untuk mendata pasien mana yang belum bayar
        yang_belum_bayar.append(pasien_hari_ini["nama"]) #jika pasien belum bayar, maka akan masuk ke dalam list yang_belum_bayar
        total_belum_bayar += yang_belum_bayar # total_yang_belum_bayar merupakan jumlah dari pasien yang belum bayar
    else: 
        return #kembalikan
    print( "=== PASIEN BELUM BAYAR ===") #membuat header untuk tabel PASIEN BELUM BAYAR
    for i in yang_belum_bayar: #melakukan perulangan untuk setiap i di list yang_belum_bayar
        print(f"{i + 1}. {i["nama"]}") #menampilkan nama - nama pasien yang belum bayar 
    
    print("Total Belum Bayar : ", total_belum_bayar) #menampilkan total jumlah pasien

tampilkan_pasien() #memanggil fungsi menampilkan data pasien
filter_belum_bayar() #memanggil fungsi yang belum bayar


#2. MEMBUAT TUPLE DAN SET

def info_klinik(): #membuat fungsi info_klinik yang membuat informasi tetap
    informasi_tetap = ("Klinik Sehat Bersama", 
                       "Jl. Merdeka No. 10, Pekanbaru", 
                       "0761-12345") #membuat tuple dimana informasi itu tidak bisa diubah

    print("Info Klinik: ") #menampilkan judul info klinik
    print(f"Nama : {informasi_tetap[0]}") #mengambil index ke 0 dari informasi_tetap yaitu Nama
    print(f"Alamat : {informasi_tetap[1]}") #mengambil index ke 1 dari informasi_tetap yaitu Alamat
    print(f"Telp : {informasi_tetap[2]}") #mengambil index ke 2 dari informasi_tetap yaitu Telp
info_klinik() #menampilkan info_klinik

def rekap_penyakit(): #membuat fungsi merekap penyakit
    jenis_penyakit_unik = set(pasien_hari_ini) #membuat set pasien_hari_ini

    for i in jenis_penyakit_unik: #melakukan perulangan untuk setiap i di jenis_penyakit_unik
        print(f"Jenis Penyakit Unik : {i}") #menampilkann data jenis penyakit unik
    
    jumlah_jenis_penyakit = len(jenis_penyakit_unik) #jumlah_jenis_penyakit adalah panjang dari jenis_penyakit_unik

    print(f"Jumlah jenis penyakit: {jumlah_jenis_penyakit}") #menampilkan jumlah_jenis_penyakit
    
    print("Rekap per penyakit: ") #membuat judul untuk merekap per penyakit
    #BELUM SIAP MASIH BLM TAU NI SKIP DULU YA
rekap_penyakit() #merekap penyakit

def cadangan():
    print("Jneis Penyakit Unik: (Flu, Tifus, Maag) \n Jumlah Jenis Penyakit : 3")
    print("Rekap per Penyakit: ")
    print("Flu : 2 pasien \n Tifus : 2 pasien \n Maag : 2 pasien")
    print("Penyakit terbanyak : Flu, Tifus, Maag (2 pasien)")

#3. OOP
class Pasien: #membuat kelas pasien
    def __init__(self, id, nama, penyakit): #membuat def init
        self.__id = id #atribut private id
        self.__nama = nama #atribut private nama
        self.__penyakit = penyakit #atribut private penyakit
    
    def tampilkan_info(self): #fungsi menampilkan informasi pasien
        pass

    def hitung_pasien(self): #fungsi menghitung pasien
        pass

p1 = Pasien
p1.tampilkan_info()
p1.hitung_pasien()

class pasienPrioritas: #membuat class pasienPrioritas
    def __super__(Pasien):
        pass


#4. Single Linked List : Antrian Pasien 
class Node:
    pass

class AntrianPasien:
    def __init__(self, dictionary): #membuat method __init__
        self.data = dictionary
        self.next = None
    
    def tambah(self):
        pass

    def tampilkan(self):
        pass

    def panggil_berikutnya(self):
        pass

    def hapus_berdasarkan_id(self, id):
        pass

    def hitung(self):
        pass
