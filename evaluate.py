class Evaluate:

    def check_win(self, array):

        last_entry = 0
        re = 0
        last_entry = array[len(array) - 1]
        if len(array) > 2:
            for i in range(0, len(array) - 1):
                # print("for")
                if last_entry + array[i] < 15:
                    if 15 - (last_entry + array[i]) in array and 15 - (last_entry + array[i]) != array[i]:
                        if 15 - (last_entry + array[i]) != last_entry:
                            re = 1
                            return re
            return re
        return re

    def systemChances(self, array):

        chances_for_system = []
        if len(array) > 1:
            for i in range(0, len(array) - 1):
                if array[len(array) - 1] + array[i] < 15:
                    chances_for_system.append(15 - (array[len(array) - 1] + array[i]))
            return chances_for_system
        else:
            return []

