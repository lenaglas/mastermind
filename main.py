import itertools
import math
import random
import re
from itertools import product
from termcolor import colored

colours = "rbtypw"
length = 5
possible_combinations=math.pow(5,len(colours))

def create_random_combination():
    random_combination = "".join(random.choice(colours) for j in range(length))
    return random_combination


def display_as_colours(string):
    str = "print("

    for i in string:
        if i == "r":
            str = str + "(colored('\u2022', 'red')), "
        if i == "b":
            str = str + "(colored('\u2022', 'blue')), "
        if i == "t":
            str = str + "(colored('\u2022', 'cyan')), "
        if i == "y":
            str = str + "(colored('\u2022', 'yellow')), "
        if i == "p":
            str = str + "(colored('\u2022', 'magenta')), "
        if i == "w":
            str = str + "(colored('\u2022', 'white')), "

    str = str + ")"
    exec(str)

def print_blacks_and_whites(checksum):
    print("this is my answer: ")
    print(checksum[0]*'\U0001f41e',checksum[1]*'\U0001f41b')


def check_combination(new_try, compare_try):
    blacks = [0, 0, 0, 0, 0]
    whites = [0, 0, 0, 0, 0]
    black = 0
    white = 0

    for index1, i in enumerate(compare_try):
        for index2, j in enumerate(new_try):
            if j == i:
                if index1 == index2:
                    blacks[index2] = 1
                    black = black + 1

    for index1, i in enumerate(compare_try):
        skip = 0
        if blacks[index1] == 0:  # only consider positions that havent been marked as black before
            for index2, j in enumerate(new_try):
                if i == j and blacks[index2] == 0 and whites[index2] == 0 and skip == 0:
                    white = white + 1
                    whites[index2] = 1
                    skip = 1

    checksum = [0, 0]
    checksum[0] = black
    checksum[1] = white
    return (checksum)


master_combination = create_random_combination()

print("Welcome to mastermind. This is a little game for your entertainment. I just have chosen a combination consisting of ", len(colours), " at ", length)
print("positions. I can choose a colour as often as I want. It can appear, ", length, "times or not at all. It is your goal to find this combination.")
print("You start with guessing the combination with giving a guess of colours in a certain order.")
print("Then I give you a hint of my combination with putting a ladybug for every colour you guessed at the right position and a centipede for every correct colour at a wring position.")
print("Possible colours are", colored('red (r)', 'red'), colored('blue (b)', 'blue'), colored('turquise (t)', 'cyan'), colored('yellow (y)', 'yellow'), colored('pink (p)', 'magenta'), "and", colored('white (w)', 'white'))
print("A possible combination inout could look like \"rbwpp\"")


found = 0


first_try=input("Your combination please:\n")
while(len(first_try)!=5 or not re.match("^[r,b,t,y,p,w]*$", first_try)):
    print("This looks wrong to me. A valid combination has consists of five digits containing any of the colours red(r), blue(b), turquoise(t), yellow (y), pink (p) or white(w)")
    first_try = input("Give me a valid combination:\n")

print("Voila, this is how your combination looks like: ")
display_as_colours(first_try)


current_checksum = check_combination(first_try, master_combination)
print_blacks_and_whites(current_checksum)

valid_combos = []
counter = 0
for combo in product(colours, repeat=length):
    combination = ''.join(combo)
    check = check_combination(combination, first_try)
    if check == current_checksum:
        counter = counter + 1
        valid_combos.append(combination)

print(counter, " combinations left")

steps = 1
while found != 1 :
    steps = steps + 1
    #choice = random.choice(valid_combos)
    choice=input("Another try please:\n")
    while (len(choice) != 5 or not re.match("^[r,b,t,y,p,w]*$", choice)):
        print(
            "This looks wrong to me. A valid combination has consists of five digits containing any of the colours", colored('red (r)', 'red'), colored('blue (b)', 'blue'), colored('turquise (t)', 'cyan'), colored('yellow (y)', 'yellow'), colored('pink (p)', 'magenta'), "and", colored('white (w)', 'white'))
        choice = input("Give me a valid combination:\n")

    if choice not in valid_combos:
        print("you made a mistake my friend. If you would have checked my answers you would knew that this combination cannot be valid. \U0001f926")
    display_as_colours(choice)
    new_checksum = check_combination(choice, master_combination)
    print_blacks_and_whites(new_checksum)

    for i in valid_combos:
        check = check_combination(i, choice)
        if (check != new_checksum):
            valid_combos.remove(i)

    combos_left = len(valid_combos)
    print(combos_left, "combinations left")
    if (combos_left == 1 or new_checksum[0]==5):
        print("")
        print("hooray, combination found in ", steps, " steps: ")
        display_as_colours(valid_combos[0])
        found = 1

print("The master combination was: ")
display_as_colours(master_combination)
