# name = input('Isimgizni kiriting:\n>>> ')
# print(f"Salom {name}")
# number = int(input("Yoshingizni kiritin \n >>>"))
# print(f"Siz {number} yoshda ekansiz")

# young  = int(input("Yoshingizni kiritung"))\


# if young >= 18 :
#   print('Siz voyaga yetgan ekansiz')
# else:
#   print('Siz voyaga yetmagan ekansiz')


# ball = int(input('balingizni kiriting\n>>>'))
# if ball >= 90 :
#   print("A'lo")
# elif ball >= 70:
#   print("yashi")
# elif ball >= 50:
#   print('Qoniqarli')
# else:
#   print("Yiqildingiz")


# for i in range(5):
#   print(i)


# mevalar = ['olma', 'anor', 'nok']
# for meva in mevalar:
#   print(f"men {meva}ni yahshi korman")

# for i in range(0, 10 , 2):
#   print(i)

# ism = input("ismingizni kiriting \n >>>")
# son = int(input("necha marta salomlashay?\n>>>"))


# if son < 5:
#   print("keling kamida 5 marotaba salom lashamiz")
#   son = 5
# elif son > 10:
#   print("bu juda kop keling 10 marta bil cheklanamiz")
#   son = 10
# else:
#   print("juda ajoyib")


# for i in range(son):
#   print(f"salom{ism}!  (#{i+1})")
# yigindi = 0
# N = int(input("Nechta son kiritasiz"))
# for n in range(N):
#   son = int(input(f"{n+1}- soni kiriting"))
#   yigindi +=son
# print(" Yig'indi javobi",yigindi)
# print(f"javolar ortacha qiymati{yigindi / N}")
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ism = ['ali', 'vali', 'hasan', 'husan', 'olim', 'umid', 'sobir', 'sardor', 'sardor', 'sardor']
# aralash = [ 1, "salom,", 2.34]

# sonlar.append(4)
# # print(sonlar)
# sonlar.extend([2, 3])
# # print(sonlar)

# print(sonlar)
# # sonlar.remove(3)
# # print(sonlar)
# # ohirgi_son = sonlar.pop(3)
# # print(ohirgi_son)
# # print(sonlar)
# sonlar.sort()
# print(sonlar)
# sonlar.sort(reverse=True)
# print(sonlar)
# print(len(sonlar))\
# sonlar[1] = 3
# print(sonlar)
# print(sonlar[2:5])
# for ismlar in ism:
#   print(f"salom {ismlar} ")
# for i in range(len(ism)):
#   print(f"{i+1} - ism  {ism[i]}")


# ism = []
# print("5 ta sim kiriting!")
# for i in range(5) :
#   ismlar = input(f"{i+1} -simni kiriting")
#   ism.append(ismlar)
# print("kiritilgan isimlar:",ism)
son1 = []
son2 = []
juftlar = []
print("5 ta son kiritng")
# for i in range(5):
#   son1qabul = int(input(f"{i+1}- soni kiriting"))
#   son1.append(son1qabul)
# print(f"qabul qilingan sonlar{son1}")
# son1 = list(range(0,32,1))
sanash = int(input("son kiriting"))
son1 = list(range(0,sanash+1,1))
# for d in range(len(son1)):d
#   son2.append(son1[d]*2)
#   # print(son2)
# print(f"kiritlgan sonlar{son1} va shu sionlarning 2 ga kopaytmasi {son2}")
for juft in son1:
  if juft % 2 == 0:
    juftlar.append(juft)
# print(f"{son1} \n ichidan juft sonlar  {juftlar}")
for s  in son1:
  print(f" bu tartibdagi sonlar{s}")
for f in juftlar:
  print(f" bu tartibdagi juft sonlar sonlar{f}")
