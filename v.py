class Evaluate:


    def check_win(self, array):

        last_num = 0
        re = 0
        last_num = array[len(array)-1]  # type: object
        if len(array)>2:
            for i in range(0, len(array)-1):
                # print("for")
                if last_num+array[i] < 15:
                    if 15-(last_num + array[i]) in array and 15-(last_num + array[i]) != array[i]:
                        if 15-(last_num + array[i]) != last_num:
                            re = 1
                            return re
            return re
        return re


    def evaluate_user(self, array):

        arr = []
        if len(array)>1:
            for i in range(0, len(array)-1):
                if array[len(array)-1] + array[i] < 15:
                    arr.append(15 - (array[len(array)-1] + array[i]))
            # print(arr)
            return arr
        else:
            return []


csss = Evaluate()