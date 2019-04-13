# Joseph Wilder (j.m.wilder715@gmail.com)
# April 13, 2019
# ======================================

#
# @brief bottom up mergesort implementation
# @param list -- the list of elements to be sorted
# @return a new list with all elements in sorted order
#
def mergesort( list ):
	rightList = []
	leftList = []

	# base case
	if len(list) == 1:
		return list;

	# divide into two lists
	for e in list:
		if list.index(e) < len(list)/2:
			leftList.append(e)
		else:
			rightList.append(e)
	
	# recurse
	leftList = mergesort(leftList)
	rightList = mergesort(rightList)
	
	return merge(leftList, rightList)	

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

unsortedIntList = [3, 15, 2, 21, 25, 14, 1, 19, 43, 10]
sortedIntList = mergesort(unsortedIntList)

unsortedCharList = ["c", "z", "a", "x", "e", "b", "r", "l"]
sortedCharList = mergesort(unsortedCharList)

print "Unsorted Integer List: " + str(unsortedIntList)
print "Sorted Integer List: " + str(sortedIntList)

print "Unsorted Char List: " + str(unsortedCharList)
print "Sorted Char List: " + str(sortedCharList)