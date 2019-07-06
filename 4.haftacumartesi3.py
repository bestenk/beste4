# dışarıdan aldığı isim ve soyisim göre mail adresi oluşturan metot
#isim.soyisim@bilgeadam.com
# kullanıcı 2.parametrede değer göndermeyebillir.

def mail (isim , soyisim = None):
    mail = ""
    if soyisim is None:
        mail = "{}@bilgeadam.com".format(isim,soyisim)
    else :
        mail = "{}.{}@bilgeadam.com".format(isim.lower(),soyisim.lower())
    print(mail)

mail(input("lütfen adınızı girin :"))
mail(input("lütfen adınızı girin :"),input("lütfen soyadınızı girin :"))

# beste.karademir@bilgeadam.com
#çağrı.çağırma@bilgeadam.com
#murat.@bilgeadam.com

