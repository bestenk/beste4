# DIŞARIDAN GİRİLEN İLK KELİMENİN İLK İKİ HARFİNİ BÜYÜK GERİ KALANINI KÜÇÜK ALINIZ
# İKİNCİ KELİMENİN İÇERİSİNDE GEÇEN TÜM A HARFLERİNİ E İLE DEĞİŞTİRİNİZ
# VE SONUNDA @HOTMAİL.COM EKLEYEREK GERİ DÖNDÜRÜNÜZ...


def Mail (isim, soyisim):
    isim_ = isim[0:2].upper() + isim[2:].lower()
    print(isim_)
    soyisim_ = soyisim.replace("a","e")
    return "{}.{}@hotmail.com".format(isim_,soyisim)
mail = Mail("beSTE", "karademir")
print("mail adresiniz :",mail)
