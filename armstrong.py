sayi=input("BİR SAYI GİRİNİZ: ")
x=len(sayi)
toplam=0

for i in sayi:
    sayi = int(sayi)
    i=int(i)
    eleman=i**x
    toplam+=eleman

if (toplam==sayi):
    print("BU BİR ARMSTRONG SAYISIDIR!!!")
else:
    print("BU BİR ARMSTRONG SAYISI DEĞİLDİR!!!")


