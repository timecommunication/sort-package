# quick sort

import random


class Quick:

    def __init__(self, comparable):

        self.comparable = comparable
        self.low = 0
        self.high = len(comparable)-1

    def shuffle(self):

        self.comparable = random.sample(self.comparable, self.high+1)

    def exchange(self, index1, index2):

        self.comparable[index1], self.comparable[index2] = \
            self.comparable[index2], self.comparable[index1]

    def partition(self, low, high):

        i, j = low, high+1
        split_ele = self.comparable[low]
        while True:

            while self.comparable[i+1] < split_ele:
                i += 1
                if i == high:
                    break
            else:
                i += 1
            while split_ele < self.comparable[j-1]:
                j -= 1
                if j == low:
                    break
            else:
                j -= 1
            if i >= j:
                break
            self.exchange(i, j)
        self.exchange(low, j)
        return j

    def sort(self, low, high):

        if high <= low:
            return
        partition = self.partition(low, high)
        self.sort(low, partition-1)
        self.sort(partition+1, high)


if __name__ == '__main__':

    alpha_instance = ['Q', 'U', 'I', 'C', 'K', 'S', 'O', 'R', 'T',
                      'E', 'X', 'A', 'M', 'P', 'L', 'E']
    q = Quick(alpha_instance)
    q.shuffle()
    q.sort(0, q.high)
    print(q.comparable)



