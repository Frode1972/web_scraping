from random import randint
from timeit import repeat
import matplotlib.pyplot as plt
from sort_lib import bubble_sort, quicksort, insertion_sort
from txt_files import load_dict_from_file


def graf(x_numbers, y1_times, y2_times, y3_times):
    '''Imports 4 lists, x_numbers is the numbers on x axis. Then lists of 3 different time measurements
    from the sorting algorithms '''
    plt.autoscale(True)
    plt.plot(x_numbers, y1_times, 'r', label="Insertion sort")
    plt.plot(x_numbers, y2_times, 'g', label="Quick sort")
    plt.plot(x_numbers, y3_times, 'b', label="Bubble sort")
    plt.xlabel('N')
    plt.ylabel('Time in seconds')
    plt.legend()
    plt.show()


def run_sorting_algorithm(algorithm, array):
    '''Set up the context and prepare the call to the specified
    algorithm using the supplied array.'''
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({array})"
    # Execute the code 10 different times and return the time
    # in seconds that each execution took
    rep = 10  # repetitions
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=rep)
    # Store the times in a list. 
    y_times.append(min(times)/rep) 
    # Display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)/rep}")


def init(array, i):
    '''Call the function using the name of the sorting algorithm
        and the array created. The array is the range of numbers to be tested'''
    if __name__ == "__main__":       
        if i == 0:
            run_sorting_algorithm(algorithm="insertion_sort", array=array)
        elif i == 1:
            run_sorting_algorithm(algorithm="quicksort", array=array)
        elif i == 2:
            run_sorting_algorithm(algorithm="bubble_sort", array=array)

L=[]
# List of measured times
y_times = []
# Numbers on x-axis
x_numbers = [int(x) for x in range(100, 2301, 200)]

# unsorted img size list from xkcd.com made in web_scraping.py
try:
    L = load_dict_from_file()
except FileNotFoundError:
    print("\nThe file unsorted.txt do not exist. You have to run web_scraping first to make a list of unsorted image file size numbers.")
    print("Instead a list of type int(x) for x in range(1,2301,1) will be made and sorted")
    input("press enter to continue")
    serie = [int(x) for x in range(1, 2301, 1)]
    for i in range(len(serie)):
        line = {"nummer": i, "size": serie[i]}
        L.append(line)


# Different types of sorting methods i=0 call insertion sort, i=1 call quicksort
# and i=2 call bubble sort.
sorting_methods = 3
for i in range(sorting_methods):
    print(i)
    y_times = []
    for x_number in x_numbers:
        array_length = []
        array_length = L[:x_number]  # Extract the number of sizes to be sorted.
        init(array_length, i)  # Call the init function.
    if i == 0:
        y1_times = y_times
    elif i == 1:
        y2_times = y_times
    elif i == 2:
        y3_times = y_times
graf(x_numbers, y1_times, y2_times, y3_times)
