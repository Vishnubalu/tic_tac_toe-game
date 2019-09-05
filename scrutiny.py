class Scrutiny:

    def __init__(self, simple_table, magic_square, player):
        self.simple_table = simple_table
        self.magic_square = magic_square
        self.first_player = player
        # system = 1
        # user = 0

    def inspect(self, system, player):

        if(self.first_player == 1):
            data = dict(list(zip(['SYS', 'VIS'], [system, player])))
        else:
            data = dict(list(zip(['VIS', 'SYS'], [player, system])))
        if(input('Do you want to review the game y/n: ') == 'y'):
            Scrutiny.evaluation(self, data=data)
        else:
            return 0


    def evaluation(self, data):
        dis = [
            "*", "*", "*",
            "*", "*", "*",
            "*", "*", "*"
        ]
        players = list(data.keys())
        positions = list(data.values())

        while True:
            if(len(positions[0]) and input("press space to continue :") == ' '):
                print('{} move : '.format(players[0]))
                dis[self.magic_square.index(positions[0][0])] = players[0]
                positions[0].pop(0)
                Scrutiny.display(self, dis)

            if(len(positions[1]) and input("press space to continue :") == ' '):
                print('{} move : '.format(players[1]))
                dis[self.magic_square.index(positions[1][0])] = players[1]
                positions[1].pop(0)
                Scrutiny.display(self, dis)
            else:
                print('The end')
                break


    def display(self, dis):
        print("\n")
        for i in range(len(dis)):
            if (i + 1) % 3 == 0:
                print(dis[i])
                print("\n")
            else:
                print(dis[i], end="\t\t")