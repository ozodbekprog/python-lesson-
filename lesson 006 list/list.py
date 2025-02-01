# lesson 006 list
# author Ozodbek

# radius = 10
# ism = 'mahmut'


mevalar = ['olma', 'anjir', 'orik']
# print(mevalar)
narxlar = [12000, 18000, 109000, 22000, -0.4]
# print(narxlar)

sonlar = [ 'bir ', 'ikki', 3, 4, 5]
ismlar = [ ]
# print(ismlar,\n sonlar)
# print(f"{sonlar}\n{ismlar}")
# print(mevalar[0])
# print(mevalar[-3].title())
# print(narxlar[0]+narxlar[1])
# print(mevalar)
# mevalar[0] = 'anor'
# print(mevalar)
# mevalar[-1] = 'uzuzm'
# print(mevalar)


# mevalar.append('tarvuz')
# print(mevalar)
# mevalar.insert(0,'banan')
# print(mevalar)
# cars = []
# cars.append('lasetti')
# cars.append('damaz')
# cars.append('tico')
# cars.append('del')
# print(cars)
# del cars[0]
# print(cars)
# cars.insert(0,'nexdiya 3')
# print(cars)
# cars.remove('tico')
# print(cars)


# hayvonlar = [ 'it', 'mushuk', 'qoy', 'fil', 'sher', 'ot', 'ot']
# print(hayvonlar)
# hayvonlar.remove('ot')
# print(hayvonlar)

# bozorlik = ['yog', 'un ', 'shakar', 'tuhum', 'margarin', ]
# print(bozorlik)
# mahsulot = bozorlik.pop(1)
# print(mahsulot)
# print(bozorlik)
# bozorlik = ['yog', 'un ', 'shakar', 'tuhum', 'margarin', ]
# mahsulot = bozorlik.pop(3)
# print(f"men {mahsulot} sotib oldim")
# print(f"olinlagan mashulotlar {bozorlik}")
# mahsulot2 = bozorlik.pop()
# print(mahsulot2)

# narxlar.remove(-0.4)
# print(narxlar)

#  homework


# task  1
# friends = ['ozodbek', 'samir', 'fariza']
# print(f"salom {friends[2]} bugun choyhona bormi? " )
# print(f"{friends[1]}, choyhonaga bormamizmi ?")


# task 2
# number = [ 10, -3, 4.0,5.6 ]
# print(number)
# print(number[0]+number[3])
# onli_numbers = number.pop(1)
# number.append(35)
# number.insert(0,13)
# print(onli_numbers)
# print(number)


# task 3
# t_shahsalar = [ 'beruniy', 'buhoriy', 'amur temur']
# z_shahslar = ['elon mask ', 'bil gats ', 'stiv jobs']
# z_shahslar_k = z_shahslar.pop(0)
# t_shahslar_k = t_shahsalar.pop(2)
# print(f"Men tarihiy shahslardan {t_shahslar_k} bilan zamonaviy shahslardan  esa {z_shahslar_k} bilan suhbat qilishni istamyman ")


# task 4
friends = []
friends.append('ozodbek')
friends.append('samir')
friends.append('fariza')
friends.append('sardor')
print(friends)
friends.remove('ozodbek')
print(friends)
friends.insert(0,'doston')
friends.insert(2,'shohruh')
friends.insert(3,'jamshit')
print(friends)
mehmonlar =[]
mehmonlar.append(friends.pop(2))
mehmonlar.append('doston')
mehmonlar.append(friends.pop(0))
print(f"\nKelgan mehmonlar{mehmonlar}")
print(f"\ndostlar{friends}")