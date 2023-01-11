#program sistem pembelian tiket pesawat
import os

while True:

    jumlahData = int(input("Masukkan jumlah data (maksimal 4) = "))

    if jumlahData > 4:
        print ("Jumlah data maksimal 4!\n")
    else:
        break



namaPesawat = {
    'LA':'Lion Air',
    'BA':'Batik Air',
    'CL':'Citilink',
    'GA':'Garuda Indonesia'
}

kotaTujuan = {
    'BTH':'Batam',
    'SUB':'Surabaya',
    'DPS':'Denpasar'
}

lionAir = {
    'DPS':731000,
    'BTH':1000000,
    'SUB':674500
}

batikAir = {
    'DPS':843500,
    'BTH':1000000,
    'SUB':833000,
}
citilink = {
    'DPS':743000,
    'BTH':988000,
    'SUB':833000
}

garudaIndonesia = {
    'DPS':1869000,
    'BTH':1931000,
    'SUB':1568000
}

tabelTiket = {
    'LA':lionAir,
    'BA':batikAir,
    'CL':citilink,
    'GA':garudaIndonesia
}

template = {
    'noPenerbangan':000,
    'kdPesawat': "XXX",
    'nmPesawat':"XXX",
    'kdTujuan': "XXX",
    'daerahTujuan':"XXX",
    'hargaTiket':000,
    'jumlahTiket':000,
    'Discount':000,
    'totalBayar':000
}

index = 0

i = 0
dictData = {}
while i < jumlahData:

    print (f"Input ke-{i}")
    
    datatmp = dict.fromkeys(template.keys())
    datatmp['noPenerbangan'] = int(input("No Penerbangan = "))
    datatmp['kdPesawat'] = input("Kode Pesawat = ")
    
    #ambil nama pesawat
    pesawat = str(datatmp['kdPesawat'])
    nama = str(namaPesawat.get(pesawat))
    datatmp['nmPesawat'] = nama

    datatmp['kdTujuan'] = input("Kode Tujuan = ")

    #ambil daerah tujuan
    daerah = str(datatmp['kdTujuan'])
    namaD = str(kotaTujuan.get(daerah))
    datatmp['daerahTujuan'] = namaD

    #harga tiket
    harga = int(tabelTiket[pesawat][daerah])
    datatmp['hargaTiket'] = harga

    datatmp['jumlahTiket'] = int(input("Jumlah Tiket = "))
    jmlTiket = int(datatmp['jumlahTiket'])

    jumlahBayar = harga * jmlTiket
    
    if jumlahBayar > 10000000:
        diskon = 25
        diskontmp = jumlahBayar * 25/100
        jumlahBayar = jumlahBayar - diskontmp

    elif jumlahBayar > 7500000:
        diskon = 15
        diskontmp = jumlahBayar * 15/100
        jumlahBayar = jumlahBayar - diskontmp

    elif jumlahBayar > 5000000:
        diskon = 10
        diskontmp = jumlahBayar * 10/100
        jumlahBayar = jumlahBayar - diskontmp
    else:
        diskon = 0

    datatmp['Discount'] = diskon

    datatmp['totalBayar'] = jumlahBayar


    key = f"data{index}"
    index+=1


    dictData.update({key:datatmp})
    i+=1

print (110*"-")
print (f"{'No':<5}|{'Kode Pesawat':<12}|{'Nama Pesawat':<17}|{'Kode Tujuan':<11}|{'Daerah Tujuan':<13}|{'Harga Tiket':<11}|{'Jumlah Tiket':<12}|{'Discount':<8}|{'Total Bayar':<11}|")
print (110*"-")
for data in dictData:
    KEY = data
    NO = dictData[KEY]['noPenerbangan']
    KODEPESAWAT = dictData[KEY]['kdPesawat']
    NAMAPESAWAT = dictData[KEY]['nmPesawat']
    KODETUJUAN = dictData[KEY]['kdTujuan']
    DAERAHTUJUAN = dictData[KEY]['daerahTujuan']
    HARGATIKET = dictData[KEY]['hargaTiket']
    JUMLAHTIKET = dictData[KEY]['jumlahTiket']
    DISKON = dictData[KEY]['Discount']
    TOTALBAYAR = dictData[KEY]['totalBayar']

    print (f"{NO:<5}|{KODEPESAWAT:<12}|{NAMAPESAWAT:<17}|{KODETUJUAN:^11}|{DAERAHTUJUAN:<13}|{HARGATIKET:<11}|{JUMLAHTIKET:^12}|{DISKON:^8}|{TOTALBAYAR:<11}|")
print (110*"-")
    

#https://github.com/mahadidn    

