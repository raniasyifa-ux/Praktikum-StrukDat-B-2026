from colorama import Fore, Back, Style, init
init()

print(Fore.RED + "Teks Merah")
print(Fore.GREEN + 'Teks HIjau')
print(Fore.BLUE + Back.YELLOW + "Teks Biru, Teks Kuning")
print(Style.RESET_ALL + 'Kembali Normal')