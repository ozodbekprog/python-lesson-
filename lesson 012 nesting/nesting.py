#  nesting
car0 = {
    'make': 'Toyota',
    'model': 'Corolla',
    'year': 2020,
    "colors": "Red"
    }

car1 = {
    'make': 'Honda',
    'model': 'Civic',
    'year': 2021,
    "colors": "Blue"
    }

car2 = {
    'make': 'Ford',
    'model': 'Mustang',
    'year': 2022,
    "colors": "Black"
    }
#  dificult way
# car = car0
# print(f"{car['make'].title()},"
#       f"{car['colors']} rangi,"
#       f"{car['year']} yili")



#  easy way
# cars = [car0, car1, car2]


# for car in cars:
#   print(f"{car["make"].title()},"
#         f"{car["colors"]} rangi,"
#         f"{car["year"]} yili")


# print(cars[1]['colors'])\




#  for

malibus = []

for n in range(10):
  new_car ={
    'make': 'Chevrolet',
    'model': 'Malibu',
    'year': 2023,
    "colors": None,
    "cost": None,
    "mileage": None,
  }
  malibus.append(new_car)
for malibu1 in malibus[0:3]:
   malibu1["colors"] = "Green"
for malibu2 in malibus[3:6]:
   malibu2["colors"] = "Black"
for malibu3 in malibus[6:]:
   malibu3["colosrs"] = "Red"
   malibu3["mileage"] = 10000
for malibu_cost in malibus:
   if malibu_cost["colors"] == "black":
      malibu_cost["cost"] = 5000
   elif malibu_cost["mileage"] <=300
   malibu_cost[""]
   else:
      malibu_cost["cost"] = 4500











for malibu in malibus:
   print(malibu)