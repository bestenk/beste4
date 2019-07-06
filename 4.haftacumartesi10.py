#dışarıdan bir sayısal dizisinin parametre olarak alan bir metot yazınız. metot parametredeki dizide yer alan elemanları toplamının karekökünü döndürsün
# import_math kelimesi içerde var olan herhangi bir kütüphaneyi eklemek için kullanırız


def karekökhesapla(sayilar):
    toplam = 0
    for sayi in sayilar :
        toplam += sayi
    return math.sqrt(toplam)





sonuc = karekökhesapla([1,2,3,4,5,6,7,8])
print("işlem sonucu :",sonuc)