# shell sort
# h-sequence: 1, 4, 13, 40, 121, 364, 1093, ...


class Shell:

    def sort(self, comparable):
        length = len(comparable)
        h = 1
        while h < int(length/3):
            h = 3*h + 1
        while h >= 1:
            for i in range(h, length):
                move_ele_index = i
                while move_ele_index >= h and \
                        comparable[move_ele_index] < comparable[move_ele_index-h]:
                    comparable[move_ele_index-h], comparable[move_ele_index] = \
                        comparable[move_ele_index], comparable[move_ele_index-h]
                    move_ele_index -= h
            h = h//3
        return comparable


if __name__ == '__main__':

    alpha_instance = ['S', 'H', 'E', 'L', 'L', 'S', 'O', 'R', 'T',
                      'E', 'X', 'A', 'M', 'P', 'L', 'E']
    shell = Shell()
    print(shell.sort(alpha_instance))

