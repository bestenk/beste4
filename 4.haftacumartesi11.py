# kullanıcı dışardan dilediği kadar sayı girsin her sayıyı girdikten sonra sayı girmeye devam edip etmeyeceği sorulacak
# kullanıcı y Y tuşuna basarsa yeni sayı girmesi istenir
# kullanıcı harici bir tuşa basar ise içeriye aldığı sayılar içerisindeki yer alan en büyük ve en küçük sayının birbirine olan farkını geriye dönecek


def sayi():
    go_on = "y"
    tek_sayilar = []
    while go_on == "y" or go_on == "Y":
        number = float(input("sayı girin :"))
        if number % 2 != 0:
            tek_sayilar.append(number);
        go_on = input("yeni bir sayı eklemek istiyor musunuz (Y\\N): ")

    return max(tek_sayilar) - min(tek_sayilar)
sonuc = sayi()
print("işlem sonucu :",sonuc)