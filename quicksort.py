# Joseph Wilder (j.m.wilder715@gmail.com)
# April 14, 2019
# ======================================

from datetime import datetime

unsortedList = [3, 1, 5, 6, 4, 2, 12, 1, 77, 10, 0, 31, 82, 97, 9, 17, 94, 65, 12, 19, 6, 2, 29, 90, 70, 66, 13, 15, 54, 29, 19, 22, 56, 45, 
				18, 9, 91, 51, 62, 71, 21, 25, 55, 31, 29, 82, 81, 74, 19, 18, 34, 101, 77, 33, 11, 6, 52, 94, 64, 27] 

def quicksort(inputList, low, high):
	if low < high :
		p = partition(inputList, low, high)
		quicksort(inputList, low, p - 1)
		quicksort(inputList, p + 1, high)

	return inputList

def partition(inputList, low, high):
	# arbitrarily choosing the last element to be pivot
	pivot = inputList[high]
	i = low
	for j in range(low, high):
		if inputList[j] < pivot:
			inputList[i], inputList[j] = inputList[j], inputList[i]
			i = i + 1
	inputList[high], inputList[i] = inputList[i], inputList[high]
	return i

if __name__ == '__main__':
	timeStart = datetime.now()
	sortedList = quicksort(unsortedList, 0, len(unsortedList) - 1)
	timeFinish = datetime.now()
	delta = timeFinish - timeStart

	print "Unsorted List: " + str(unsortedList)
	print "Sorted List:   " + str(sortedList)
	print "Total time to sort in ms: " + str(delta.total_seconds() * 1000)