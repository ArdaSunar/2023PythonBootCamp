## String => Metinsel İfade
baslik = "Konut Kredisi"
print(baslik)

baslik = "Taşıt Kredisi"
print(baslik)

## int, integer => tam sayı ifade etmek için kullanılır
vade = 36

## float, decimal, double => ondalıklı sayı ifade etmek için kullanılır
aylikOdeme = 200.50

##bool, boolean => True/False verilerini tutar.
dolarYukseldiMi = True
euroYukseldiMi = False

## Matematiksel Operatorler => 4 işlem dahil olmak üzere matematiksel işlemler yapmak üzere kullanılan bir çok operatör vardır.

print((((5+5)*2)/20)-1) ## Örnekteki gibi 4 işlemi tek bir satırda yapmak mümkün.

toplamKredi = vade*aylikOdeme
print("Toplam borcunuz: " + str(toplamKredi) + "'dir.")

fiyat = 100

indirimliFiyat = fiyat - 20

print(indirimliFiyat)

# % => mod operatörü(x % 5 denkleminde, x sayısının 5'e bölümünden sonra kalan sayıyı çıktı verir.)
print(15%5) ## 15 sayısı 5'e tam bölündüğünden çıktı 0 olacaktır.
print(16%5) ## 16 sayısının 5'e bölümünde kalan 1 olduğundan çıktı 1 olacaktır.


# mantıksal operatörler => True veya False(Boolean) olarak çıktı verir.

print(1 == 1) # 1, 1'e eşit mi sorusunun cevabını çıktı olarak verecektir.
print(1 == 2) # 1, 2'ye eşit mi sorusunun cevabını çıktı olarak verecektir.

print(1>2) # 1, 2'den büyük mü sorusunun cevabını çıktı olarak verecektir.
print(1>=1) # Büyük eşittir.

print(1!=1) #!=, eşit değildir operatörüdür.

print(1!=2)

# or and

print(1>2 or 5>2) ## or(veya) operatöründe iki ifadeden birinin True(doğru) olması durumunda çıktı True olarak verilir.

print(1>2 and 5>2) ## and(ve) operatöründe, çıktının True olması için her iki ifadenin de True olması gerekmektedir.

# karar yapıları
#if else

sayi1 = 10
sayi2 = 20
## sayi1 sayi2'den büyükse 1. koşulu, eşitse 2. koşulu, diğer her koşulda 3. koşulu çalıştırır.
if sayi1>sayi2:
     print("Büyüktür") 
elif sayi1 == sayi2:
     print("Eşittir")
else:
     print("Muhtemelen küçüktür")







