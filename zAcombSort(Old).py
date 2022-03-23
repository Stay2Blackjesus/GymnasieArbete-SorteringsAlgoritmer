import time
import random
array = []


def Randomizer(x):

    start = round(time.time()*1000)

    for x in range(x):
     global array
     array.append(random.randint(1,1000))

    end = round(time.time()*1000)
    print (f'Making Random list = {end-start}ms')

def GreekbubbleSort(array):
  x = round(time.time()*1000)  
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
  y = round(time.time()*1000)
  print (f'GreekBubblesort = {y-x}ms')

def BubbleSort(arr):
    a = round(time.time()*1000) 
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    b = round(time.time()*1000)
    print (f'bubblesort = {b-a}ms')   


Randomizer(1000)
BBL = array
GBBL = array


GreekbubbleSort(GBBL)
BubbleSort(BBL)


input("hello")

#Old startAverage()
def startAverage(n,v):
    bbl = 0
    ins = 0
    sel = 0
    mer = 0
    qui = 0
    r = 15
    for x in tqdm(range(n)):
        Randomizer(v)
        bbl+=timeit(bubbleSort,number=r)/r
        ins+=timeit(insertionSort,number=r)/r
        sel+=timeit(selectionSort,number=r)/r
        mer+=timeit(mergeStarter,number=r)/r
        qui+=timeit(quickSortStarter,number=r)/r
    print(f'bubbleSort    = {round(bbl/n*1000,3)}ms')
    print(f'insertionSort = {round(ins/n*1000,3)}ms')
    print(f'selectionSort = {round(sel/n*1000,3)}ms')
    print(f'mergeSort     = {round(mer/n*1000,3)}ms')
    print(f'quickSort     = {round(qui/n*1000,3)}ms')