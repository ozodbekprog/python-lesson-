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
cars = [car0, car1, car2]


for car in cars:
  print(f"{car["make"].title()},"
        f"{car["colors"]} rangi,"
        f"{car["year"]} yili")