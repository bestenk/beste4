# kullsnıcı dışarıdan string olarak sayı dizisi gönderecek
# 3 4 5 6 77.7 77 4 12.3 54 54.67 gibi

#gelen string değeri geriye sayısal bir dizi olarak döndürünüz






def converttolist(string):
    mylist = string.split()
    for n in range(len(mylist)):
        if mylist[n].count("."):
           mylist[n] = float(mylist[n])
        else:
            mylist[n] = int(mylist[n])

    return mylist


result = converttolist("3 4 5 6 77.7 77 4 12.3 54 54.67")
print(result)




