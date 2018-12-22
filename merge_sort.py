# merge sort Top-down


class Merge:

    def __init__(self, comparable):
        self.origin = comparable
        self.origin_low = 0
        self.origin_high = len(comparable)-1
        self.aux = [i for i in self.origin]

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

    def sort(self, low, high):

        if high <= low:
            return
        middle = low + (high - low) // 2
        self.sort(low, middle)
        self.sort(middle+1, high)
        self.merge(low, middle, high)


if __name__ == '__main__':

    alpha_instance = ['M', 'E', 'R', 'G', 'E', 'S', 'O', 'R', 'T',
                      'E', 'X', 'A', 'M', 'P', 'L', 'E']
    length = len(alpha_instance)
    m = Merge(alpha_instance)
    m.sort(m.origin_low, m.origin_high)
    print(m.origin)

