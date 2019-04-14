# Joseph Wilder (j.m.wilder715@gmail.com)
# April 13, 2019
# ======================================
from datetime import datetime

unsortedList = [3, 1, 77, 10, 0, 31, 82, 97, 9, 17, 94, 65, 12, 19, 6, 2, 29, 90, 70, 66, 13, 15, 54, 29, 19, 22, 56, 45, 
				18, 9, 91, 51, 62, 71, 21, 25, 55, 31, 29, 82, 81, 74, 19, 18, 34, 101, 77, 33, 11, 6, 52, 94, 64, 27] 

#
# @brief inefficient bubblesort of an unsorted list
# @param inputList -- the list to be sorted
# @return a sorted list of everything in inputList
#
def bubblesort( inputList ):
	sortedList = []
	
	# O(n^2) complexity ...  
	for i in range(0, len(inputList) - 1):
		for j in range (0, len(inputList) - 1):
			if inputList[j] > inputList[j + 1]:
				inputList[j], inputList[j + 1] = inputList[j + 1], inputList[j]
	return inputList

if __name__ == '__main__': 
	print "Unsorted List: " + str(unsortedList)

	timeStart = datetime.now()
	sortedList = bubblesort(unsortedList)
	timeFinish = datetime.now()
	delta = timeFinish - timeStart

	print "Sorted List:   " + str(sortedList)
	print "Total time to sort in ms: " + str(delta.total_seconds() * 1000)

