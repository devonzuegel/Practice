''' PROBLEM: Given an array of integers, return the subsets whose sum is equal to 0 '''

''' PSEUDOCODE:
		if sofar sums to goal, add to subsets
		if len(rem) == 0 return subsets
		else recurse with and without first in rem
		extend subsets to include results of recursing
		return subsets	'''


# returns a list of sets from rem that sum up to goal
def subsets_with_sum_rec(rem, sofar, goal):
	subsets = []

	if (sum_of(sofar) == goal):		subsets.append(sofar)

	if (len(rem) != 0):
		# recurse WITHOUT the first elem of remaining
		subsets_without = subsets_with_sum_rec(rem[1:], sofar, goal)
		subsets.extend(subsets_without)

		# recurse WITH the first elem of remaining
		subsets_with = subsets_with_sum_rec(rem[1:], sofar + [rem[0]], goal)
		subsets.extend(subsets_with)

	return subsets

# finds the sum of an array
def sum_of(array):
	sum = 0
	for x in array:		sum += x
	return sum

# given a list, returns list with no duplicate entries
def remove_duplicity(list):
	result = []
	for x in list:
		if x not in result:		result.append(x)
	return result

# returns a list of sets from list that sum up to goal
# if no_duplicates == true, returns only unique sets; NOTE: [1,0]==[1,0] but [1,0]!=[0,1]
def subsets_with_sum(list, goal, no_duplicates):
	subsets = subsets_with_sum_rec(list, [], goal)

	if no_duplicates:  return remove_duplicity(subsets)
	else:							 return subsets

# -----------------------------------------
# TEST RUNS:

arr = [1, 0, 1]
goal = 1
no_duplicates = True

print("result = " + str(subsets_with_sum(arr, goal, no_duplicates)) )