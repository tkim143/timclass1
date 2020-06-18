
#Make an array for the sorting of the selection

array = [13, 4, 9, 5, 3, 16, 12]

def selectionSort(array):
#function header

	n = len(array)
	#n variable is length of the array

	for i in range(n): #whatever length of the array is how many times youre going to run the loop

	#intially assume the first element of the unsorted part as the minimum

		minumum = i

		for j in range(i+1, n):

		if (array[j]) < array[minumum]:

		minimum = j

	#swap the minimum element with the 

	temp = array[i]
	array[i] = array[minimum]
	array[minimum] = temp
	#pushing lowest number first and pushing the rest back
	return array

print(selectionSort(array))
