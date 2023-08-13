import random

def generate_roulette():
    return list(range(0, 36 + 1))

def spin_roulette(roulette_list):
    number = random.choice(roulette_list)
    return number

def is_red(roulette_number):
    print("The roulette number is", roulette_number)
    if roulette_number % 2 != 0:
        print("The number in the roulette is red, you win!")
    else:
        print("The number in the roulette isn't red, you lose")

def is_black(roulette_number):
    print("The roulette number is", roulette_number)
    if roulette_number % 2 == 0:
        print("The number in the roulette is black")

def is_zero(roulette_number):
    print("The roulette number is", roulette_number)
    if roulette_number == 0:
        print("The number in the roulette is 0 ")

def choice_number(number, roulette_number):
    print(f'The number in the roulette is {roulette_number}')
    if number == roulette_number:
        print("The number in the roulette is the same that you choice, you win!")
    elif number != roulette_number:
        print("The number in the roulette isn't the same that you choice, you lose!")
    
