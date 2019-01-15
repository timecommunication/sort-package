# lambda version of quick sort
import random

l = [i for i in range(10)]
random.shuffle(l)
quick_sort = lambda array: array if len(array) <= 1 else quick_sort(
    [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
    [item for item in array[1:] if item > array[0]])

print(l)
print(quick_sort(l))