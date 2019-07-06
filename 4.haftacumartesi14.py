def mail(ad:str, soyad:str, domain:str = "bilgeadam")-> str :

    return "{}.{}@{}".format(ad,soyad,domain)



#mail("beste","karademir","hotmail")

#print(type(mail("","")))
print(mail("beste","karademir","hotmail"))
print("mail metodunun geriye dönüş tipi : ",mail.__annotations__)

#beste karademir bilgeadam
#beste karademir hotmail