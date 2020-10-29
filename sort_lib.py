import timeit
from random import randint


def bubble_sort(alist):
    '''Bubblesort'''
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i]["size"] < alist[i+1]["size"]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return(alist)


def insertion_sort(L):
    '''Insertion sort'''
    for i in range(1, len(L)):
        item_to_insert = (L[i])
        #print(item_to_insert)
        j = i-1
        while j >= 0 and L[j]["size"] < item_to_insert["size"]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = item_to_insert
    return L

def quicksort(array):
    '''Quicksort'''
    if len(array) < 1:
        return array
    low, same, high = [], [], []
    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item["size"] > pivot["size"]:
            high.append(item)
        elif item["size"] == pivot["size"]:
            same.append(item)
        elif item["size"] < pivot["size"]:
            low.append(item)
    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(high) + same + quicksort(low)