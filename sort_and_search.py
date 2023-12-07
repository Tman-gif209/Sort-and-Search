#Using the following array: [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
#Create a Python script called sort_and_search.py
#Which searching algorithm would be appropriate to use on the given list?
Searching_algorithm = "Linear search"

#Implement this searching algorithm to search for the number 9. Add a comment to explain why you think this algorithm was a good choice.
def sequential_search(item, arr):

    for i in range(len(arr)):
        if arr[i] == item:
            return i

searching = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
print(sequential_search(9, searching))

explanation = "I think this algorithm was a good choice because elements are not in order and we have an element that we want and so we will be going through th list comparing each element to the know element."

#Research and implement the Insertion sort on this array.
def insertionSort(list):
    for step in range(1, len(list)):
        key = list[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        list[j + 1] = key

insertionSort(searching)
print(searching)
#Implement a searching algorithm you haven’t tried yet in this Task on the sorted array to find the number 9. Add a comment to explain where you would use this algorithm in the real world.
searching.sort()

def binary_search(item, arr):
    low, high = 0, len(arr) - 1
# Keep iterating until low and high cross
# Returns None if item not found
    while high >= low:
# Find midpoint
        mid = (low + high) // 2
# If item is found at midpoint, return
        if arr[mid] == item:
            print(arr[mid])
            return mid
# Else, if item at midpoint is less than item,
# search the second half of the list
        elif arr[mid] < item:
            low = mid + 1
# Else, search first half
        else:
            high = mid - 1

print(binary_search(9, searching))

answer = "Best to use since the list is in order and we know which element we wan we can simply just go to the element."
