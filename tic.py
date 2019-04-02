
import v
import random
import numpy as np


class Main:
    table = list([8, 3, 4, 1, 5, 9, 6, 7, 2])
    dis = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
    system = list([])
    player = list([])
    ret = list([])


def display():
    print("\n\n")
    for i in range(len(main.dis)):
        if (i+1) % 3 == 0:
            print(main.dis[i])

            print("\n\n")
        else:
            print(main.dis[i], end="\t\t")

def system_time():
    n = []
    if len(main.table) == len(main.system)+len(main.player):
        print(" ------- DRAW MATCHING----------")
        return 0
    else:
        if 2 <= len(main.system):
            n = check.evaluate_user(main.system)
        count = 0
        for value in n:
            if value in main.table and value not in main.system and value not in main.player:
                n = n
                count = count+1
                break;
        if(count == 0):
            n = check.evaluate_user(main.player)
    entry_of_system(n)



def entry_of_system(n):
    # print(n)
    while True:
        # print("while")
        if len(n) == 0:
            if(len(main.player) == 1):
                o = int(random.choice([8,4,5,6,2]))
            else:
                o = int(random.choice(np.arange(1, 9)))
            if (o not in main.system) and (o not in main.player):
                # print("system input", o)
                break
        else:
            for i in n:
                if i not in main.system and i not in main.player and i in main.table:
                    o = i
                    # print("system", o)
                    break
            else:
                while True:
                    o = int(random.randint(1, 9))
                    if (o not in main.system) and (o not in main.player):
                        # print("system input", o)
                        break
            break

    main.system.append(o)
    main.dis[main.table.index(o)] = "SYS"

    display()
    if check.check_win(main.system) == 0:
        entry_of_player()
    else:
        print("********* system win *********")


def entry_of_player():
    if len(main.table) == len(main.system)+len(main.player):
        print("DRAW MATCHING")
        return 0
    else:
        def taking_input():
            try:
                user_input = int(input(" VIS move : "))
                return user_input;
            except:
                print("An error occured @ please insert integer value :")
                taking_input()
        x = taking_input()
        while True:
            try:
                if (main.table[x - 1] not in main.system) and (main.table[x - 1] not in main.player):
                    break;
                else:
                    print("already choosen $ ")
                    x = taking_input()
            except:
                print("Please insert integer ranges from(1-9)")
                x = taking_input()
                break


        # print(x)
        main.player.append(main.table[x - 1])
        main.dis[x - 1] = "VIS"
        # print(check.check_win(main.player))
        if check.check_win(main.player) == 0:
            system_time()
        else:
            print("*********YOU WON**********")


            check = v.Evaluate()  # type: Evaluate
main = Main()

if __name__ == "__main__":
    while True:
        print(" Table View : ")
        display()
        # select_player = input("who place first : ")
        if(input("who place first s/u: ").lower() == 'u'):
            entry_of_player()
        else:
            system_time()
        print("Do you want to play again (y/n) : ")
        if input().lower() == 'n':
            break;
        main.dis = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
        main.system = list([])
        main.player = list([])
        main.ret = list([])
    print("Thanks for using")
