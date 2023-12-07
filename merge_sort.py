#Modify the Merge sort algorithm to order a list of strings by string length from the longest to the shortest string. This is the result of me modifying it
def merge_sort(items):
    
    items_2 = []; items_3=[]
    for i in items:
        items_2.append([i,len(i)]) #seperating each string in the list
    items_2.sort(key = lambda x : x[1], reverse=True) #ordering the strings by length from shortest to largest
    for i in items_2:
        items_3.append(i[0]) #adding the ordered strings into a new list which will be the result.
    return items_3

#Run the modified Merge sort algorithm against 3 string lists of your choice. Please ensure that each of your chosen lists is not sorted and has a length of at least 10 string elements.
string_1 = ('burger', 'dog', 'chicken', 'cucumber', 'tomato', 'pythagoras', 'mom', 'dad', 'daughter', 'son')
print(merge_sort(string_1))

string_2 = ('pillow', 'bed', 'bedroom', 'bathroom', 'tv', 'two', 'three', 'door', 'key', 'lock')
print(merge_sort(string_2))

string_3 = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
print(merge_sort(string_3))