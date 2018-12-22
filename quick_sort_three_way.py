# quick sort 3-way
import random


class QuickThreeWay:

    def __init__(self, comparable):

        self.comparable = comparable
        self.low = 0
        self.high = len(comparable)-1

    def shuffle(self):

        self.comparable = random.sample(self.comparable, self.high+1)

    def exchange(self, index1, index2):

        self.comparable[index1], self.comparable[index2] = \
            self.comparable[index2], self.comparable[index1]

    def sort(self, low, high):

        if high < low:
            return
        less, equal, greater = low, low+1, high
        split_ele = self.comparable[low]

        while equal <= greater:

            if self.comparable[equal] < split_ele:
                self.exchange(less, equal)
                equal += 1
                less += 1
            elif self.comparable[equal] > split_ele:
                self.exchange(equal, greater)
                greater -= 1
            else:
                equal += 1
        self.sort(low, less-1)
        self.sort(greater+1, high)


if __name__ == '__main__':

    alpha_instance = ['R', 'B', 'W', 'W', 'R', 'W', 'B', 'R', 'R', 'W', 'B', 'R']

    qtw = QuickThreeWay(alpha_instance)
    qtw.shuffle()
    qtw.sort(qtw.low, qtw.high)
    print(qtw.comparable)
