import evaluate
import random
class GUI_evaluate:
    def __init__(self):
        self.check = evaluate.Evaluate()
        self.table_values = list([
            8, 3, 4,
            1, 5, 9,
            6, 7, 2])
        self.system_entries = list([])

    def check_for_winner(self, player_entries):
        global stop_game
        stop_game = False
        if len(player_entries) > 2 and self.check.check_win(player_entries) != 0:
            stop_game = True
            tk.messagebox.showinfo("WINNER!", "YOU ARE THE WINNER /n CONGRATULATIONS")
        if len(self.system_entries) > 2 and self.check.check_win(self.system_entries) != 0:
            stop_game = True
            tk.messagebox.showinfo("WINNER", "YOU LOST, SYSTEM WON THE GAME /n TRY AGAIN")
        if len(self.table_values) == len(self.system_entries) + \
                len(player_entries):
            stop_game = True
            tk.messagebox.showinfo("WINNER", "THIS MATCH IS TIE")
        return stop_game

    def calculateSystemChances(self, player_entries):
        chances_for_system = []

        if len(self.system_entries) >= 2:
            chances_for_system = self.check.systemChances(self.system_entries)
        no_chances = 0

        for value in chances_for_system:
            if value in self.table_values and \
                    value not in self.system_entries and \
                    value not in player_entries:
                chances_for_system = chances_for_system
                no_chances = no_chances + 1
                break

        if no_chances == 0:
            chances_for_system = self.check.systemChances(player_entries)
        r, c = gui.entry_of_system(chances_for_system, player_entries)
        return (r, c)

    def entry_of_system(self, chances_for_system, player_entries):

        while True:
            if len(chances_for_system) == 0:
                if len(player_entries) == 1:
                    system_choice = int(random.choice([8, 4, 5, 6, 2]))
                else:
                    system_choice = int(random.choice(np.arange(1, 9)))
                if (system_choice not in self.system_entries) and (system_choice not in player_entries):
                    break
            else:
                for choice in chances_for_system:
                    if choice not in self.system_entries and choice not in player_entries and choice in self.table_values:
                        system_choice = choice
                        break
                else:
                    while True:
                        system_choice = int(random.randint(1, 9))
                        if (system_choice not in self.system_entries) \
                                and (system_choice not in player_entries):
                            break
                break
        self.system_entries.append(system_choice)
        system_choice = self.table_values.index(system_choice)
        r, c = system_choice // 3, system_choice % 3
        return r, c

gui = GUI_evaluate()