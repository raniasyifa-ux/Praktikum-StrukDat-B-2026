#kita akan mengimport module kurs ke konverter terlebih dahulu

from kurs import mataUang

#membuat fungsi konverter IDR ke mata uang 

def IDR_ke_uangAsing (IDR, uangAsing):
    if uangAsing in mataUang:
        return IDR / mataUang[uangAsing]
    else:
       return None

def uangRandom_ke_mataUang (jumlahKonver, UangAsing):
    if UangAsing in mataUang:
        return jumlahKonver * mataUang[UangAsing]
    else:
      return  None
