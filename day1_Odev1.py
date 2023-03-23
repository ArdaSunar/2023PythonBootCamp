## Metinsel veri tipi => string olarak geçer ve iki tırnak("") arasına yazılan ifadelerden oluşur.

metinOrnegi = "Merhaba Dünya!"
print(metinOrnegi)

## Sayısal veri tipleri => int(tam sayı), float(ondalıklı sayı) gibi veri tipleridir. Sayısal ifadeleri içlerinde tutar.

sayi1 = 10 #int
sayi2 = 10.5 #float

## Boolean/Bool => True/False çıktısı veren veri tipidir. Bir koşulun doğruluğuna göre çıktı verir.

sayi1 = 5
sayi2 = 7

print(sayi1 > sayi2) #sayi1, sayi2'den büyük olmadığı için çıktımız False olacaktır.
print(sayi1 < sayi2) #sayi1, sayi2'den küçük olduğu için çıktımız True olacaktır.

## Sekans veri tipleri => Sıralı verileri içlerinde barındırır.
#list => sayısal veya metinsel farketmeksizin farklı verileri içlerinde barındırırlar.

liste1 = ["Ahmet", "Ayşe", "Arda"]
print(liste1) #Listeyi tamamıyla yazdıracaktır.

print(liste1[0]) #listenin sadece "[]" içerisinde belirtilen elemanını çağıracaktır.

liste2 = [1, 2, 3] #Listeler ayrıca sayısal ifadeleri de saklar.
print(liste2) #Listeyi tamamıyla yazdıracaktır.

print(liste2[0]) #listenin sadece "[]" içerisinde belirtilen elemanını çağıracaktır.

#range => belirli bir sıradaki sayıları içinde tutar. for döngüsü kullanılarak içindeki tüm elemanlar yazdırılabilir.

dizi1 = range(1,100) #virgülden önceki sayı ile virgülden sonraki sayı arasında bir dizi oluşturur.

for i in dizi1:
    print(dizi1[i-1])

dizi2 = range(1,100,2) #ilk örneğe ek olarak virgülden sonra eklenen sayı, dizinin kaçar kaçar artacağını belirler.

for i in range(0,len(dizi2)): #len komutu, bir veri setinin içinde kaç karakter bulunduğunun çıktısını vermektedir.
    print(dizi2[i])

#********************************************

## kodlama.io sitesindeki değişkenler.

kullaniciAdi = "Arda"
aldigiDersler = "Python"
derseKatilim = True

if derseKatilim == True:
    print(kullaniciAdi + " gets a cookie.")
else:
    print(kullaniciAdi + " get a dayak.")

