Assignment Web Scraping


1	What the program does
The delivery includes four files, which are web_scraping.py, plot.py, sort_lib.py and txt_files.py. 
1.1	Plot.py file
The plot.py file try to load meta data from dict.txt, which is made by the web_scraping.py program. But the file is made only if the web_scraping.py is executes first. If dict.txt exists, the plot.py will use it for time measuring the sorting algorithms. Else if the dict.txt do not exist the plot.py makes its own test range. 
Then the program uses the lists made in the sorting algorithms, that is insertion sort, quick sort and bubble sort.  The sorting algorithms are explained under the plot section. The program then measures the time use for each of the sorting algorithms. The time y axis is plotted for x in range (100, 2301, 200). 
The sorting algorithms are imported from sort_lib.py and the dict.txt is loaded from a function in txt_files.py.
1.2	Web_scraping.py file
The program starts to check if dict.txt exist, which is the file of the images metadata in xkcd.com, that is, size, name and URL of each image. If the dict.txt do not exist, the program start downloading metadata from each image in �xkcd.com� and store it in the variable �img_liste� as dictionary in list and then save it as dict.txt. 
The program then sorts the list by using quicksort algorithm, the list is sorted descending by size. From the plot.py I found out that it was the fastest sorting algorithm. The sorting algorithms are in the sort_lib.py .  After the sorting, the program fetches the first ten largest images and print them to the screen with image name and file size. 
The user then selects on of the images, if the image do not exist in the ./xkcd/ folder it will be downloaded from the xkcd.com, else if the image exists in the folder it will be loaded from the folder. The image will be shown.
1.3	Sort_lib.py
Containing three functions, the bubble sort, insertion sort and quicksort.
1.4	 txt_files.py
The file includes two functions the save_dict_to file which saves the dict.txt file including the meta data from the images and the load_dict_from_file which load the dict file.
2	Libraries used


 
Figure 1 Y axis is the measured time and x axis is the number of sorted elements.
The plot is based on a list of 2300 elements from the image sizes and the sorting time of 100, 300, 500 and up to 2300 elements. The timeit library is used for measuring the times. In this plot it is used 1000 numbers of repetitions. 
We can see on the graph that the Quick sort is the most effective sorting algorithm and in this case, it seems almost linear horizontally. But It should be n*log(n) graph, but it is a lot more effective than the two other methods, so it seems flat in comparison. 
3.2	Bubble sort
Bubble sort has two for loops and a complexity of n^2. The n is the number of items being sorted. It starts from an end and repeatedly compare each pair of adjacent values and swap them if they are not in descending order. It keeps doing this until there are no more values to swap.
3.3	Insertion sort
Insertion sort has a for loop and while loop and is also an n^2 sorting algorithm, but it is more effective than the bubble sort. It starts sorting from an end and then split the list in a sorted and unsorted part, the values are taken from the unsorted part and placed correctly in the sorted part.
3.4	Quick sort
Quick sort has an average performance of n*log(n) and is more effective than the bubble sort and the insertion sort. Quick Sort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the list elements into lower and higher array around the pivot number. It splits the array into smaller arrays until it ends up with an empty array, or one that has only one element. It is a recursive function and call itself until it is done.
