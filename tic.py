
import v
import random
import numpy as np


class Main:
    table = list([8, 3, 4, 1, 5, 9, 6, 7, 2])
    dis = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
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
    else:
        if 2 <= len(main.system):
            n = check.evaluate_user(main.system)
        if len(n) == 1 and n[0] not in main.system and n[0] not in main.player:
            if n[0] in main.table:
                n = n
            else:
                n = check.evaluate_user(main.player)
        else:
            n = check.evaluate_user(main.player)
        entry_of_system(n)



def entry_of_system(n):
    # print(n)
    while True:
        # print("while")
        if len(n) == 0:
            o = int(random.choice(np.arange(1, 10)))
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
                    o = int(random.randint(1, 10))
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
    else:

        x = int(input(" VIS move : "))
        while True:
            if (main.table[x - 1] not in main.system) and (main.table[x - 1] not in main.player):
                break;
            else:
                x = int(input("already choosen $ VIS move : "))
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
print(" Table View : ")
display()
entry_of_player()
print("vishnu")
