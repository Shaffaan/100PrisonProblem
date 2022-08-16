import random
import matplotlib.pyplot as plt


# first task is to generate a randm list of numbers 1-100
def generate_random_list(sizze: int) -> list:
    lst = []
    while len(lst) != sizze:
        x = random.randint(0, sizze - 1)
        if x not in lst:
            lst.append(x)

    return lst


# Second task is 1 game for 100 prisoner:
def game() -> list[bool]:
    # create the random list and assign it to a variable

    random_list = generate_random_list(100)

    # main loop

    lst = []
    prisoner_number = 0
    while prisoner_number < len(random_list):
        # I will be the length of the longest loop

        def recursive_function(the_number_of_box: int, the_number_of_the_prisoner: int) -> bool:
            # base case
            if the_number_of_box == 0:
                #Number of boxes opened is zero
                #means all 50 boxes have been opened
                return False
            else:
                y = random_list[the_number_of_the_prisoner]
                if prisoner_number == y:
                    return True
                else:
                    return recursive_function(the_number_of_box - 1, random_list[the_number_of_the_prisoner])

        x = recursive_function(50, prisoner_number)
        lst.append(x)
        prisoner_number += 1
    return lst


# plays the game x amount of times

def runner(x) -> float:
    games_played = 0
    games_won = 0
    i = 0
    while i < x:
        temp_answer = game()
        if all(temp_answer):
            games_won += 1
            games_played += 1
            i += 1
        else:
            i += 1
            games_played += 1
    return (games_won / games_played) * 100


def graphher():
    times_the_function_is_rerun = []
    probability = []
    i = 0
    while i < 300: # x axis list is from 0 - 1000 (probaility gets better)
        i += 1
        times_the_function_is_rerun.append(i)
        probability.append(runner(i))
    plt.plot(times_the_function_is_rerun, probability)
    plt.show()
