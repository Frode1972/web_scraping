import timeit
from random import randint

def insertion_sort(L):
    for i in range(1,len(L)):
        item_to_insert =(L[i])
        j=i-1       
        while j>=0 and L[j] < item_to_insert:
            L[j+1] = L[j]
            j -=1
        L[j+1] = item_to_insert
    #print("insertion_sort",L[:10])    	   
    return L        

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
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
        if item > pivot:
            high.append(item)
        elif item == pivot:
            same.append(item)
        elif item < pivot:
            low.append(item)
    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list   
    return quicksort(high) + same + quicksort(low)

def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    #print("bubble_sort",alist[:10])
    return(alist)
	

	
