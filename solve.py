def bolenleri_bul(sayi):
    bolen_listesi = []
    for i in range(1,sayi+1):
        if (sayi % i == 0):
            bolen_listesi.append(i)
    return bolen_listesi
liste = []
n = int(input("Lütfen kat sayisini giriniz: "))

for i in range(n):
    if len(bolenleri_bul(i+1)) % 2 ==0:
        print(i+1, ". katın lambası kapali")
    else:
        print(i+1, ". katın lambası acik")
    liste.append(len(bolenleri_bul(i+1)) % 2)
print("Acik lamba sayisi", sum(liste), "\nKapali lamba sayisi", n-sum(liste))