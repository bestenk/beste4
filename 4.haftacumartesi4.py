# dışarıdan aldığı metin içerisindeki sesli karakterlerin ve sessiz karakterlerin sayısını ekrana yazdıran metot

def seslikontrolü (string):
    sesli_kontrolü = ["a","e","i","ı","ö","o","u","ü"]
    liste = list(string)
    seslicount = 0
    sessizcount = 0
    count = len(liste)
    for i in liste:
        if i in sesli_kontrolü:
            seslicount += 1
        else:
            sessizcount += 1
    print("toplam sesli harf sayısı : {}\ntoplam sessiz harf sayısı : {}".format(seslicount, sessizcount))
seslikontrolü("dawwweopdkdkloeaöı")
