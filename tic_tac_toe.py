import evaluate
import random
import numpy as np


class Game:
    table_values = list([
        8, 3, 4,
        1, 5, 9,
        6, 7, 2])
    dis = [
        "*", "*", "*",
        "*", "*", "*",
        "*", "*", "*"
    ]
    system_entries = list([])
    player_entries = list([])


def display():
    print("\n\n")
    for i in range(len(obj.dis)):
        if (i + 1) % 3 == 0:
            print(obj.dis[i])
            print("\n\n")
        else:
            print(obj.dis[i], end="\t\t")


def calculateSystemChances():
    chances_for_system = []
    if len(obj.table_values) == len(obj.system_entries) + len(obj.player_entries):
        print(" ************ DRAW MATCH ************")
    else:
        if len(obj.system_entries) >= 2:
            chances_for_system = check.systemChances(obj.system_entries)
        no_chances = 0

        for value in chances_for_system:
            if value in obj.table_values and value not in obj.system_entries and value not in obj.player_entries:
                chances_for_system = chances_for_system
                no_chances = no_chances + 1
                break

        if no_chances == 0:
            chances_for_system = check.systemChances(obj.player_entries)
    entry_of_system(chances_for_system)


def entry_of_system(chances_for_system):
    """
    :type chances_for_system: an array having all the favarable chances for system
    to place next step

    Function evaluates the chances and chooses best position to place next step
    """
    while True:
        if len(chances_for_system) == 0:
            if len(obj.player_entries) == 1:
                system_choice = int(random.choice([8, 4, 5, 6, 2]))
            else:
                system_choice = int(random.choice(np.arange(1, 9)))
            if (system_choice not in obj.system_entries) and (system_choice not in obj.player_entries):
                break
        else:
            for choice in chances_for_system:
                if choice not in obj.system_entries and choice not in obj.player_entries and choice in obj.table_values:
                    system_choice = choice
                    break
            else:
                while True:
                    system_choice = int(random.randint(1, 9))
                    if (system_choice not in obj.system_entries) \
                            and (system_choice not in obj.player_entries):
                        break
            break

    obj.system_entries.append(system_choice)
    obj.dis[obj.table_values.index(system_choice)] = "SYS"

    display()
    if check.check_win(obj.system_entries) == 0:
        entry_of_player()
    else:
        print("********* system win *********")


def entry_of_player():
    if len(obj.table_values) == len(obj.system_entries) \
            + len(obj.player_entries):
        print("***********DRAW MATCHING*************")
    else:
        def taking_input():
            try:
                user_input = int(input(" VIS move : "))
                return user_input
            except:
                print("An error occured @ please insert integer value :")
                taking_input()

        user_choice = taking_input()

        while True:
            try:
                if (obj.table_values[user_choice - 1] not in obj.system_entries) \
                        and (obj.table_values[user_choice - 1] not in obj.player_entries):
                    break
                else:
                    print("already choosen , Chose another place")
                    user_choice = taking_input()
            except:
                print("Please insert integer ranges from(1-9)")
                user_choice = taking_input()
                break

        # print(x)
        obj.player_entries.append(obj.table_values[user_choice - 1])
        obj.dis[user_choice - 1] = "VIS"
        # print(check.check_win(obj.player))
        if check.check_win(obj.player_entries) == 0:
            calculateSystemChances()
        else:
            print("*********YOU WON**********")


check = evaluate.Evaluate()
obj = Game()

if __name__ == "__main__":

    while True:
        print(" Table View : ")
        display()
        if input("who place first s/u: ").lower() == 'u':
            entry_of_player()
        else:
            calculateSystemChances()
        print("Do you want to play again (y/n) : ")
        if input().lower() == 'n':
            break
        obj.dis = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
        obj.system_entries = list([])
        obj.player_entries = list([])
    print("Thanks for using")
