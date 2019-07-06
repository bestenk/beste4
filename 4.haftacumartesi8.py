# dışardan girilen değerin tek veya çift olma durumuna göre geriye dönen metot sayı çift ise : -1 tek ise :1 sıfıra eşit ise : 0 değerini teslim etsin

def sayi (s1):
    if s1 == 0:
        return 0
    elif s1 % 2 == 0:
        return -1

    else:
        return 1
print(sayi(int(input("lütfen sayı girin : "))))





