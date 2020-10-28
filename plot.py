from random import randint
from timeit import repeat
import matplotlib.pyplot as plt
from sort_lib import bubble_sort, quicksort, insertion_sort
from txt_files import load_unsort

def graf(x_numbers,y1_times,y2_times,y3_times):    
    plt.autoscale(True)
    plt.plot(x_numbers, y1_times,'r',label="Insertion sort")
    plt.plot(x_numbers, y2_times,'g',label="Quick sort")
    plt.plot(x_numbers, y3_times,'b',label="Bubble sort")
    plt.xlabel('N')
    plt.ylabel('Time in seconds')
    plt.legend()
    plt.show()

def run_sorting_algorithm(algorithm, array):  
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. 
    setup_code = f"from __main__ import {algorithm}"     
    stmt = f"{algorithm}({array})"
    # Execute the code ten different times and return the time
    # in seconds that each execution too
    rep=1 #repetitions
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=rep)
    y_times.append(min(times)/rep)   
    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)/rep}")
    
def init(array,i):
    if __name__ == "__main__":                              
        # Call the function using the name of the sorting algorithm
        # and the array you just created
        if i==0:
            run_sorting_algorithm(algorithm="insertion_sort", array=array)
        elif i==1:
            run_sorting_algorithm(algorithm="quicksort", array=array)
        elif i==2:
            run_sorting_algorithm(algorithm="bubble_sort", array=array)
        #print(L[:10])

y_times=[] #List of measured times
x_numbers=[int(x) for x in range(100,2301,200)] #Numbers on x-axis

try: 
    L=load_unsort()#unsorted img size list from xkcd.com made in web_scraping.py
except:
    print("\nThe file unsorted.txt do not exist. You have to run web_scraping first to make a list of unsorted image file size numbers.") 
    print("Instead a list of type int(x) for x in range(1,2301,1) will be made and sorted")    
    input("press enter to continue")
    L=[int(x) for x in range(1,2301,1)]

sorting_methods=3 #different types of sorting methods
for i in range(sorting_methods):
    print(i)
    y_times=[]    
    for x_number in x_numbers:
        array_length=[]
        array_length=L[:x_number]
        init(array_length,i)
    if i == 0:
        y1_times=y_times
    elif i==1:
        y2_times=y_times
    elif i==2:
        y3_times=y_times        
graf(x_numbers,y1_times,y2_times,y3_times)