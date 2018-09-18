"""
Paul Vu
Data Structures and Algorithms II 
Programming Assignment 1
"""
def insertion_sort(A):
    """Merges list using insertion sort"""
    j = 1
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

def merge_sort(A):
    """Calls merge_sort_recurions"""
    merge_sort_recursion(A, 0, len(A) - 1)

def merge_sort_recursion(A, p, r):
    """Sorts left and right halves and then merges"""
    if p < r:
        q = (p + r)//2 #Midpoint
        merge_sort_recursion(A, p, q) #Sort left half
        merge_sort_recursion(A, q + 1, r) #Sort right half
        merge(A, p, q, r) #Merge left and right halves
        
def merge(A, p, q, r):
    """merges the left and right halves together"""
    L = A[p:q + 1] #Left sublist
    R = A[q + 1:r + 1] #Right sublist
    L.append(99999) #Sentinel Value
    R.append(99999) #Sentinel Value
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]: 
            A[k] = L[i] #Add left value to list if smaller than right
            i += 1 
        else:
            A[k] = R[j] #Add right value to list if smaller than left
            j += 1
