# a prior queue based on the heap structure


class MaxPQ:

    def __init__(self):

        self.keys = {}
        self.n = 0

    def is_empty(self):

        return self.n == 0

    def size(self):

        return self.n

    def smaller(self, key1, key2):

        return self.keys[key1] < self.keys[key2]

    def exchange(self, key1, key2):

        self.keys[key1], self.keys[key2] = \
            self.keys[key2], self.keys[key1]

    def swim(self, key):

        while key > 1 and self.smaller(key//2, key):

            self.exchange(key//2, key)
            key = key//2

    def sink(self, key):

        while 2*key <= self.n:

            j = key *2
            if j < self.n and self.smaller(j, j+1):
                j += 1
            if not self.smaller(key, j):
                break
            self.exchange(key, j)
            key = j

    def insert(self, value):

        self.n += 1
        self.keys[self.n] = value
        self.swim(self.n)

    def delete_max(self):

        max = self.keys[1]
        self.exchange(1, self.n)
        self.n -= 1
        del self.keys[self.n+1]
        self.sink(1)
        return max


if __name__ == '__main__':

    alpha_instance = ['H', 'E', 'A', 'P', 'S', 'O', 'R', 'T']
    mpq = MaxPQ()
    for index, value in enumerate(alpha_instance):
        mpq.insert(value)
    print(mpq.keys)
    sorted_list = []
    for i in range(len(mpq.keys)):
        sorted_list.append(mpq.delete_max())
    # Descending
    print(sorted_list)









