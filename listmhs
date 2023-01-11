import datetime as dt
import os 

#template dict mahasiswa
mahasiswaTemplate = {
    'nama':'nama',
    'nim':'0000000000',
    'sksLulus':0,
    'lahir':dt.datetime(1111,1,11)
}

dataMahasiswa = {}
a = 0
while True:
    os.system("clear")

    ##input data mhs
    print (f"{'Data Mahasiswa':^30}")
    print (40*"-")

    #mengambil dict dari template
    mahasiswa = dict.fromkeys(mahasiswaTemplate.keys())
    #input
    mahasiswa['nama'] = input ("Masukkan nama mahasiswa: ")
    mahasiswa['nim'] = input ("Masukkan nim mahasiswa: ")
    mahasiswa['sksLulus'] = int(input("Masukkan Jumlah sks: "))
    #tanggal bulan lahir
    TANGGAL = int(input("Masukkan tanggal lahir: "))
    BULAN = int(input("Masukkan bulan lahir: "))
    TAHUN = int(input("Masukkan tahun lahir: "))
    mahasiswa['lahir'] = dt.datetime(TAHUN, BULAN, TANGGAL)

    #key untuk index 'key'
    key = f"mhs{a}"

    dataMahasiswa.update({key:mahasiswa})

    a+=1
    print ("\n")
    print (f"{'Kunci':<6}|{'Nama':<19}|{'Nim':<10}|{'SKS':<3}|{'Lahir':<10}|")
    print (67*"-")

    for mhs in dataMahasiswa:
        KEY = mhs
        NAMA = dataMahasiswa[KEY]['nama']
        NIM = dataMahasiswa[KEY]['nim']
        SKS = dataMahasiswa[KEY]['sksLulus']
        LAHIR = dataMahasiswa[KEY]['lahir'].strftime("%x")

        print (f"{KEY:<6}|{NAMA:<19}|{NIM:<10}|{SKS:<3}|{LAHIR:<10}|")
        

    isLagi = input("\nApakah masih ada data? (y/t): ")

    if isLagi == 't' or isLagi == 'T':
        break

print ("\n\n===Isi data===")
print (dataMahasiswa)
