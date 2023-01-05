#belah ketupat
count = 1
sisi = int(input("Masukkan sisi ketupat = "))
spasi = int(sisi/2)

if sisi%2 == 0:
    count2 = sisi-1
else:
    count2 = sisi - 2


x = 0

while True:

    if count < sisi:
        if count%2 == 0:
            count+=1
            continue
    
        print (" "*spasi, "*"*count)
        spasi-=1
        count+=1
    else:
        if x == 0:
            spasi+=1
        x = 1
        if count2%2 != 0:
            count2-=1
            continue
        else:
            spasi+=1
            count2-=1
            print (" "*spasi, "*"*count2)

    if count2 == 1:
        break

