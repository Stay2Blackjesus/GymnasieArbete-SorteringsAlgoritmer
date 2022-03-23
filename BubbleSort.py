import time
start = time.time()
arr = []
comp = 0
# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)

	for i in range(n-1):

		for j in range(0, n-i-1):

			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				global comp
				comp += 1

# Driver code to test above


bubbleSort(arr)

end = time.time()
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i],end=",")
    
print(f'\nTime elapsed = {end - start}')
print(f'Comparisions made = {comp}')
input("Press Enter to Continue:")
