"""
Paul Vu
Data Structures and Algorithms II 
Programming Assignment 1
"""
from random import randint
import sorts

def random_list(length, min, max):
    """
    Generates a list of specified length with random
    values from min to max
    """
    lst = []
    if min == None and max == None:
        """Default Values for min and max"""
        min = 0
        max = 9
    for i in range(length):
        lst.append(randint(min, max))
    return lst

def is_sorted(list):
    """Check to see if list is sorted"""
    i = 0
    j = 1
    if(len(list) == 0 or len(list) == 1):
        return True #If length of list is 0 or 1, it is sorted
    else:
        for x in range(len(list) - 1):
            if list[i] <= list[j]:
                i+=1
                j+=1
            else:
                return False
    return True

def test_insertion_sort(shortest, longest, repitions):
    """Generates random list and tests the insertion sort"""
    for i in range(shortest, longest + 1):
        for j in range(repitions):
            randomList = random_list(i, 0, 20)#Generate random list
            sorts.insertion_sort(randomList)#Calls insertion sort
            if is_sorted(randomList):#Check if sorted
                print("SUCCESS: The list is sorted!")
            else:
                print ("FAILED: List with length " + i + " is not sorted")
                return

def test_merge_sort(shortest, longest, repitions):
    """Generates random list and tests the merge sort"""
    for i in range(shortest, longest + 1):
        for j in range(repitions):
            randomList = random_list(i, 0, 20)#Generate random list
            sorts.merge_sort(randomList)#Calls merge sort
            if is_sorted(randomList): #Check if sorted
                print("SUCCESS: The list is sorted!")
            else:
                print ("FAILED: List with length " + i + " is not sorted")
                return

print("Testing insertion sort")
test_insertion_sort(3, 5, 3) #Testing code for insertion sort
print("Testing merge sort")
test_merge_sort(3, 5, 3) #Testing code for merge sort