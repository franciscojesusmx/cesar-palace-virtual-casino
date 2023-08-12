import random

def generate_roulette():
    return list(range(0, 36 + 1))

def spin_roulette(roulette_list):
    number = random.choice(roulette_list)
    return number

def is_red(roulette_number):
    if roulette_number % 2 != 0:
        print("The number in the roulette is red")

def is_black(roulette_number):
    if roulette_number % 2 == 0:
        print("The number in the roulette is black")

roulette_list = generate_roulette()
random_number = spin_roulette(roulette_list)

print("The roulette is spinning...")
print("The number that came up is:", random_number)

is_red(random_number)
is_black(random_number)
