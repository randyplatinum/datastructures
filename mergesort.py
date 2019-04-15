# Joseph Wilder (j.m.wilder715@gmail.com)
# April 13, 2019
# ======================================

from datetime import datetime

unsortedList = [3, 1, 5, 6, 4, 2, 12, 1, 77, 10, 0, 31, 82, 97, 9, 17, 94, 65, 12, 19, 6, 2, 29, 90, 70, 66, 13, 15, 54, 29, 19, 22, 56, 45, 
				18, 9, 91, 51, 62, 71, 21, 25, 55, 31, 29, 82, 81, 74, 19, 18, 34, 101, 77, 33, 11, 6, 52, 94, 64, 27] 
				
#
# @brief bottom up mergesort implementation
# @param inputList -- the list of elements to be sorted
# @return a new list with all elements in sorted order
#
def mergesort( inputList ):

	# base case
	if len(inputList) == 1:
		return inputList;

	# divide into two lists
	middle = len(inputList)/2
	right = inputList[middle:]
	left = inputList[:middle]
	
	# recurse
	left = mergesort(left)
	right = mergesort(right)
	
	return merge(left, right)	

#
# @brief helper function that merges two sublists in sorted order
# @param leftList, rightList -- the two lists to be merged
# @return a new sorted list that contains all the elements of the sorted lists 
#
def merge(leftList, rightList):
	sortedList = []
	
	# wait for one to run out
	while (len(leftList) and len(rightList)):
		if leftList[0] < rightList[0]:
			sortedList.append(leftList.pop(0))
		else:
			sortedList.append(rightList.pop(0))
	
	# clean up anything that remains
	while(len(leftList)):
		sortedList.append(leftList.pop(0))
	while(len(rightList)):
		sortedList.append(rightList.pop(0))

	return sortedList	


if __name__ == '__main__': 
	timeStart = datetime.now()
	sortedList = mergesort(unsortedList)
	timeFinish = datetime.now()
	delta = timeFinish - timeStart

	print "Unsorted List: " + str(unsortedList)
	print "Sorted List:   " + str(sortedList)
	print "Total time to sort in ms: " + str(delta.total_seconds() * 1000)
