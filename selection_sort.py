# selection sort


class Selection:

    def sort(self, comparable):
        length = len(comparable)
        for i in range(length):
            min_ele_index = i
            for j in range(min_ele_index+1, length):
                if comparable[j] < comparable[min_ele_index]:
                    comparable[j], comparable[min_ele_index] \
                        = comparable[min_ele_index], comparable[j]
        return comparable


if __name__ == '__main__':

    number_instance = [6,5,4,3,2,1]
    alpha_instance = ['d', 'a', 'e', 'c', 'b', 'f']
    selection = Selection()
    print(selection.sort(number_instance))
    print(selection.sort(alpha_instance))

