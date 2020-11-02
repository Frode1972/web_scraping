from random import randint


def bubble_sort(alist):
    '''Bubble sort has two for loops and a complexity of n^2. 
    The n is the number of items being sorted. 
    It starts from the end and repeatedly compare each pair of 
    adjacent values and swap them if they are not in descending order. 
    It keeps doing this until there are no more values to swap.'''
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i]["size"] < alist[i+1]["size"]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return(alist)


def insertion_sort(L):
    '''Insertion sort has a for loop and while loop and is also an n^2 sorting algorithm, 
    but it is more effective than the bubble sort. 
    It starts sorting from a end and then split the list in an sorted and unsorted part, 
    the values are taken from the unsorted part and placed correctly in the sorted part.'''
    for i in range(1, len(L)):
        item_to_insert = (L[i])
        j = i-1
        while j >= 0 and L[j]["size"] < item_to_insert["size"]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = item_to_insert
    return L


def quicksort(array):
    '''Quick sort has an average performance of n*log(n) and is more 
    effective than the bubble sort and the insertion sort.'''
    if len(array) < 1:
        return array
    low, same, high = [], [], []
    # Select `pivot` element randomly
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
