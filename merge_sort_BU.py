# merge sort BU(Bottom-Up)


class MergeBU:

    def __init__(self, comparable):

        self.origin = comparable
        self.low = 0
        self.high = len(comparable)-1
        self.aux = [i for i in comparable]

    def merge(self, low, middle, high):
        i, j = low, middle+1
        for k in range(low, high+1):
            # initialize a auxiliary list
            self.aux[k] = self.origin[k]
        for k in range(low, high+1):
            if i > middle:
                # the left part had empty, use the right part
                self.origin[k] = self.aux[j]
                j += 1
            elif j > high:
                # the right part had empty, use the left part
                self.origin[k] = self.aux[i]
                i += 1
            elif self.aux[j] < self.aux[i]:
                # right part value is smaller, use the right part value
                self.origin[k] = self.aux[j]
                j += 1
            else:
                # left part value is smaller, use left part value
                self.origin[k] = self.aux[i]
                i += 1

    def sort(self):
        size = 1
        while size < self.high+1:
            low = 0
            while low < self.high+1-size:
                self.merge(low, low+size-1, min(low+size+size-1, self.high))
                low += size+size
            size += size


if __name__ == '__main__':

    alpha_instance = ['M', 'E', 'R', 'G', 'E', 'S', 'O', 'R', 'T',
                      'E', 'X', 'A', 'M', 'P', 'L', 'E']
    length = len(alpha_instance)
    mbu = MergeBU(alpha_instance)
    mbu.sort()
    print(mbu.origin)