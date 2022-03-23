from tqdm import tqdm
from tqdm import trange
from timeit import timeit
import random

unsort = []

def Randomizer(x):
    global unsort
    unsort.clear()
    for x in range(x):
     x = random.randint(1,1000)
     unsort.append(x)
    

def bubbleSort():
    global unsort
    arr = unsort.copy()
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return(arr)
    
def insertionSort():
    global unsort
    arr = unsort.copy()
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return(arr)

def selectionSort():
    global unsort
    array = unsort.copy()
    size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    return(array)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def mergeStarter():
    global unsort
    arr = unsort.copy()
    mergeSort(arr)
    return(arr)

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
def quickSortStarter():
    global unsort
    arr = unsort.copy()
    n = len(arr)
    quickSort(arr,0,n-1)
    return(arr)


def start(r):
    Randomizer(r)
    print(f'bubblesort =    {timeit(bubbleSort   ,number=100)/100*1000}ms')
    print(f'Insertionsort = {timeit(insertionSort,number=100)/100*1000}ms')
    print(f'selectionSort = {timeit(selectionSort,number=100)/100*1000}ms')

def startAverage(n,v):
    bbl = 0
    ins = 0
    sel = 0
    mer = 0
    qui = 0
    r = 10
    wbar = tqdm(total=100, desc="Complete")
    bbar = tqdm(total=100, desc="BubbleSort   ")
    ibar = tqdm(total=100, desc="InsertionSort")
    sbar = tqdm(total=100, desc="SelectionSort")
    mbar = tqdm(total=100, desc="MergeSort    ")
    qbar = tqdm(total=100, desc="QuickSort    ")
    for x in range(n):
        Randomizer(v)
        for x in range(r):
            bbl+=timeit(bubbleSort,number=1)/r
            bbar.update(int(100/r))
        for x in range(r):
            ins+=timeit(insertionSort,number=1)/r
            ibar.update(int(100/r))
        for x in range(r):
            sel+=timeit(selectionSort,number=1)/r
            sbar.update(int(100/r))
        for x in range(r):
            mer+=timeit(mergeStarter,number=1)/r
            mbar.update(int(100/r))
        for x in range(r):
            qui+=timeit(quickSortStarter,number=1)/r
            qbar.update(int(100/r))
        bbar.reset()
        ibar.reset()
        sbar.reset()
        mbar.reset()
        qbar.reset()
        wbar.update(int(100/n))
    wbar.close()
    bbar.close()
    ibar.close()
    sbar.close()
    mbar.close()
    qbar.close()

    print(f'bubbleSort    = {round(bbl/n*1000,3)}ms')
    print(f'insertionSort = {round(ins/n*1000,3)}ms')
    print(f'selectionSort = {round(sel/n*1000,3)}ms')



startAverage(10,1000)
input("Press Enter to Continue...")
