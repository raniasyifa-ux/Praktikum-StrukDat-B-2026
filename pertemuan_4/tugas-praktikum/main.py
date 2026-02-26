from kurs import mataUang as uang
from konverter import IDR_ke_uangAsing as ind
from konverter import uangRandom_ke_mataUang as bule
from tabulate import tabulate

def tampilkan_kurs():
    print('=== KONVERTER MATA UANG RANIA SYIFA ===')

    tabel = []
    for kode, nilai in uang.items():
        tabel.append([kode, f'{nilai:,}'])
    
    print(tabulate(tabel, headers=['KODE', 'KURS'],tablefmt="grid" ))


def main():
    tampilkan_kurs()

    dari = input('Dari (IDR/USD/SGD/EUR/JPY): ').upper()
    ke = input('Ke (IDR/USD/EUR/SGD/JPY): ').upper()
    
    try:
        inputan = input('Jumlah: ')
        jumlah = float(inputan.replace(".", ""))

        # DARI IDR KE MATA UANG ASING
        if dari == 'IDR' and ke in uang:
            hasilnya = ind (jumlah, ke)
            print(f'Rp {jumlah:,.0f} = {hasilnya:} {ke}')

        # DARI UANG ASING KE IDR
        elif dari in uang and ke == "IDR":
            hasil = bule(jumlah, dari)
            if hasil is not None:
                print(f'{jumlah:.2f}{dari} = Rp {hasil:,.0f}')

        else:
            print('KODE TIDAK VALID')
    except ValueError:
        print('JUMLAH WAJIB BERUPA ANGKA')

if __name__ == "__main__":
    main()
        
