cars = ['damas', 'nexia', 'tico', 'cobalt', 'nexia', 'nexia', 'audi','Nexia']
# cars.lower()
# cars.sort(reverse=True)

# print(sorted(cars, reverse=True))
# print(cars)
# random_numbers = [ 3, 5, 7, 8, 9, 1, 2, 4, 6]
# print(sorted(random_numbers, reverse=True))
# print(random_numbers)
# print(cars)
# cars.reverse()
# print(cars)
# print(len(cars))
# print(len(random_numbers))
# uzuenlik = len(random_numbers)
# print(uzuenlik)

# numbers = list(range(1,10))
# print(numbers)
# numbers2 = list(range(21,30))
# print(numbers2)
# numbers3 = list(range(21,31))
# print(numbers3)
# toq_sonalar = list(range(1,20,2))
# print(toq_sonalar)
# juft_sonalar = list(range(0,20,2))
# print(juft_sonalar)
# sanash = list(range(0,101,10))
# print(sanash)
# max_qitymat = max(toq_sonalar)
# print(max_qitymat)
# cost = [ 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
# print(min(cost))
# print(sum(cost))



diffrent_cost = [ 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
cheap_cost = min(diffrent_cost)
exepsive_cost = max(diffrent_cost)
all_cost = sum(diffrent_cost)
# print(f"eng arzon narhlar {cheap_cost} eng qimmat narhlar {exepsive_cost} jami narhlar {all_cost}")

# cars = ['damas', 'nexia', 'tico', 'cobalt', 'nexia', 'nexia', 'audi','Nexia']
# print(cars[1:])
# my_cars = cars
# print(my_cars)
# print(cars)
# my_cars.remove('nexia')
# print(my_cars)
# my_cars[0] = 'malibu'
# print(my_cars)
# print(cars)
# print(cars[2:5])
# my_cars = cars[:]
# print(my_cars)
# my_cars.remove('nexia')
# print(cars)
# print(my_cars)


# # tuple
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[-1])
# toys = list(toys)
# toys.remove('bus')
# toys = tuple(toys)
# print


# homework
# 1
country = ['uzbekistan', 'russia', 'usa', 'china', 'turkey']
# print(len(country))
# print(sorted(country , reverse=True))
# country.reverse()
# print(country)
# country.sort()
# print(country)
# country.sort(reverse=True)
# print(country)

# 2
# random_numbers = list(range(120, 1201, 2))
# big_number = sorted(random_numbers, reverse=True)
# small_number = sorted(random_numbers)
# # print(f"enga kata va eng kichi sonlar ayirmasi {big_number[0]-small_number[0]}")
# print(len(random_numbers))
# # print(sum(random_numbers))

# 3
breacfast_and_diner_foods = ['osh', 'somsa', 'shashlik', 'manti', 'somsa', 'norin', 'dimlama', 'shashlik']


print(breacfast_and_diner_foods)


mels = breacfast_and_diner_foods[1:5]
mels.appned('qozon kabob')
mels.append('shurva')
print(breacfast_and_diner_foods)
print(mels)
breacfast_and_diner_foods.tuple()
breacfast_and_diner_foods.append('qaymoq')
print(breacfast_and_diner_foods)