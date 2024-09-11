import array
import numpy as np

# Advantage of array model is that it's fast, also part of Python standard library
# Disadvantage is that it's homogeneous, so only one data type


my_array = array.array('i') # O(1) for both time and space complexity
print(my_array)

my_array1 = array.array('i', [1,2,3,4]) # O(N) for both time and space complexity
print(my_array1)

# numpy is way cooler

np_array = np.array([], dtype=int)
print(np_array)

np_array1 = np.array([1,2,3,4]) # Don't need to specify data type if you have actual data
print(np_array1)

"""""
Insertion using array model
"""""
my_array1.insert(14, 6)
print(my_array1)
# Time complexity takes however many N elements since they all need to be shifted right

"""""
Array traversal
"""""
def traverseArray(array):
	for i in array: # Time complexity is O(N) and space complexity is O(1) since no need for extra space
		print(i)

traverseArray(my_array1)

"""""
Searching for an element
"""""
def linear_search(array, target):
	for i in range(len(array)): # Time complexity of len() is O(1) btw; also O(1) for range b/c it just creates an interator
		if array[i] == target:
			return i
	return -1

print(linear_search(my_array1, 2)) # 1
print(linear_search(my_array1, 8)) # -1

"""""
Deletion
"""""
my_array1.remove(4) # O(N) T.C. and O(1) S.C. (no need for extra space)
print(my_array1) # Got rid of the 4 in the 3rd index


"""""
2D Arrays with numpy
"""""
twoDArray = np.array([ # T.C. and S.C. are both O(n^2)
	[11, 15, 10, 6],
	[10, 14, 11, 5],
	[12, 17, 12, 8],
	[15, 18, 14, 9],
	])
print(twoDArray)

"""""
2D Arrays with numpy
"""""
newtwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis = 1) # 1 is col
print(newtwoDArray)

newtwoDArray2 = np.insert(twoDArray, 0, [[1,2,3,4]], axis = 0) # 0 is row
print(newtwoDArray2)

newtwoDArray3 = np.append(twoDArray, [[1,2,3,4]], axis = 0) # append just adds to the end
print(newtwoDArray3)

newtwoDArray4 = np.append(twoDArray, [[1],[2],[3],[4]], axis = 1) # for columns
print(newtwoDArray4)

"""""
Deleting cols or rows
"""""
newtwoDArray5 = np.delete(newtwoDArray4, 4, axis = 1)
print(newtwoDArray5)


arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ") # (end = " ") just means there's not a new line, but whitespace (or in this case, a space)





