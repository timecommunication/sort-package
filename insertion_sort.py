# insertion sort


class Insertion:

    def sort(self, comparable):
        length = len(comparable)
        for i in range(1, length):
            move_ele_index = i
            for j in range(0, i):
                if comparable[move_ele_index] < comparable[j]:
                    comparable[move_ele_index], comparable[j] = \
                        comparable[j], comparable[move_ele_index]
        return comparable


if __name__ == '__main__':
    number_instance = [3,4,2,5,6,1]
    insertion = Insertion()
    print(insertion.sort(number_instance))
