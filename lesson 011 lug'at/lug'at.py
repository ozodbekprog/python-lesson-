# car_0 = {'rang':'qizil', 'yil':2018, 'narh':40000, 'km':50000, 'korobka':'avtomat'}
# # print(car_0['rang'])
# # print(car_0['yil'])
# # print(car_0['narh'])
# # print(car_0['km'])
# print(car_0['rang'],)
# en_uz = {'apple':'olma', 'pear':'nok','apricot':'o\'rik','banana':'banan'}
# mevalar = {'olma':10000, 'nok':20000, 'o\'rik':30000, 'banan':40000}
# print(f"Olma narxi {mevalar['olma']}so'm ")
# talaba_0 = {'ismi':}
# car_0 = {'model':'ferrari', 'rangi':'qizil'}
# print(car_0['model'])
# print(car_0['rangi'])
# print(f"salom bizda {car_0['model']} nomli mashina bor va bizda {car_0['rangi']} rangda")

# en_uz = {'apple':'olma', 'pear':'nok','apricot':'o\'rik','banana':'banan'}
# print(en_uz['apple'])

# # write me fruto cost list in uz
# mevalar = {'olma':10000, 'nok':20000, 'o\'rik':30000, 'banan':40000}

# # lugat talaba malumotlarini saqlash
# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
# # print(f"talaba ismi {talaba_0['ism'].title()} yoshi {talaba_0['yosh']} da tugilgan yili {talaba_0['t_yil']}da ")\
# print(f"talaba ninig ismi {talaba_0['ism'].title()} yoshi esa {talaba_0['yosh']} \
# da tugiulgan yili esa \
# {talaba_0['t_yil']}-da")

# student_0 = {
#   "name":"Tony",
#   "last_name":"Harison",
#   "age":22,
#   "class":"math",
#   "curse":4
# }
# print(student_0["name"])
# print(student_0.items())
# for key, value in student_0.items():
#   print(f"Kalit:{key}")
#   print(f"Qiymat: {value} \n")

phones ={
  "ali":"iphone x",
  "jalil":"iphone x",
  "vali":"redmi note 11 pro",
  "jamshid":"galxy s9",
  "olim":"mi 10 pro",
  "dilsor":"mi 10 pro",
  "orif":"nokia 3310",
  "jasur":"nokia 3310",
  "umar":"mi 10 pro"
}
# for k,q in phones.items():
#   print(f"{k.title()}ning tlefoni {q}")


mahsultlar = {
  "olam":10,
  "anor":11,
  "anjir":20,
  "uzum":40
}

# # print(mahsultlar.keys())

# print("Dokondagi mahsulotlar:")
# for mahsulot in mahsultlar:
#   print(f"{mahsulot.title()}")
bozorlik = []
for mahsulot in mahsultlar:
  bozorlik.append(mahsulot)
bozorlik.append("baliq")
bozorlik.append("bodring")
print(bozorlik)

# for royhat in mahsultlar:
#   if royhat in  bozorlik:
#     print(f"{royhat.title()} {mahsultlar[royhat]} so'm")
# for buyum in bozorlik:
#   if buyum not in mahsultlar:
#     print(f"Ilstimos, do'koningizga {buyum} ham olib keling")

# for masulots in sorted(mahsultlar):
#   print(masulots.title())


# print(phones.values())
# print("foydalanuvchilar quydagi tlefonlanri ishlatishadi")
# for tel in phones.values():
#   print(tel)


# print("foydlanuvchilar quydagi telefon ishlatadi")
# for tel in set(phones.values()):
#   print(tel)


#  hormwork

# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}
# for k, v in python_words.items():
#   print(f"{k.title()}   -   {v}")\


davlatlar = {
  "uzbekistan":"Toshkent",
  "BBA":"Dubai",
  "Amerika":"Washington",
  "Britaniya":"London"
}
# print("Davlatlar:")
# for davlat in sorted(davlatlar):
#   print(f"{davlat.upper()}")
# print("n\DAvlatalar poytahtalari")
# for shaharalar in sorted(davlatlar.values()):
#   print(shaharalar)

# sorov = float(input("davlat kiriting")).lower(  )

# for davlat in davlatlar.items():
#   if davlat in sorov:
#     print("")
