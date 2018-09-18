from multiprocessing import Process, Array, Queue, Pool
import ctypes
from functools import partial
import timeit


def time_results() :
    """Write any code needed to compare the timing of the sequential and parallel versions
    with a variety of string lengths."""

    T = "a" * 10
    P = "a"
    T2 = "a" * 100
    P2 = "a" * 5
    T3 = "a" * 1000
    P3 = "a" * 50
    T4 = "a" * 10000
    P4 = "a" * 500
    T5 = "a" * 100000
    P5 = "a" * 5000
    T6 = "a" * 1000000
    P6 = "a" * 50000
    P7 = "a" * 500000

    def SequentialOne():
        nonlocal T
        nonlocal P
        naive_string_matcher(T, P)
    def ParallelOne():
        nonlocal T 
        nonlocal P
        p_naive_string_matcher(T, P)
    def SequentialTwo():
        nonlocal T
        nonlocal P2
        naive_string_matcher(T, P2)
    def ParallelTwo():
        nonlocal T
        nonlocal P2
        p_naive_string_matcher(T, P2)

    def SequentialThree():
        nonlocal T2
        nonlocal P
        naive_string_matcher(T2, P)
    def ParallelThree():
        nonlocal T2
        nonlocal P
        p_naive_string_matcher(T2, P)
    def SequentialFour():
        nonlocal T2
        nonlocal P3
        naive_string_matcher(T2, P3)
    def ParallelFour():
        nonlocal T2
        nonlocal P3
        p_naive_string_matcher(T2, P3)

    def SequentialFive():
        nonlocal T3
        nonlocal P
        naive_string_matcher(T3, P)
    def ParallelFive():
        nonlocal T3
        nonlocal P
        p_naive_string_matcher(T3, P)
    def SequentialSix():
        nonlocal T3
        nonlocal P4
        naive_string_matcher(T3, P4)
    def ParallelSix():
        nonlocal T3
        nonlocal P4
        p_naive_string_matcher(T3, P4)

    def SequentialSeven():
        nonlocal T4
        nonlocal P
        naive_string_matcher(T4, P)
    def ParallelSeven():
        nonlocal T4
        nonlocal P
        p_naive_string_matcher(T4, P)
    def SequentialEight():
        nonlocal T4
        nonlocal P5
        naive_string_matcher(T4, P5)
    def ParallelEight():
        nonlocal T4
        nonlocal P5
        p_naive_string_matcher(T4, P5)

    def SequentialNine():
        nonlocal T5
        nonlocal P
        naive_string_matcher(T5, P)
    def ParallelNine():
        nonlocal T5
        nonlocal P
        p_naive_string_matcher(T5, P)
    def SequentialTen():
        nonlocal T5
        nonlocal P6
        naive_string_matcher(T5, P6)
    def ParallelTen():
        nonlocal T5
        nonlocal P6
        p_naive_string_matcher(T5, P6)
    
    def SequentialEleven():
        nonlocal T6
        nonlocal P
        naive_string_matcher(T6, P)
    def ParallelEleven():
        nonlocal T6
        nonlocal P
        p_naive_string_matcher(T6, P)
    def SequentialTwelve():
        nonlocal T6
        nonlocal P7
        naive_string_matcher(T6, P7)
    def ParallelTwelve():
        nonlocal T6
        nonlocal P7
        p_naive_string_matcher(T6, P7)
    print("n\tm\tSequential\t\tParallel")
    print("--------------------------------------------------------------------")
    print(str(len(T)) + "\t" + str(len(P)) + "\t" + str(timeit.timeit(SequentialOne, number = 1)) + "\t" + str(timeit.timeit(ParallelOne, number = 1)))
    print(str(len(T)) + "\t" + str(len(P2)) + "\t" + str(timeit.timeit(SequentialTwo, number = 1)) + "\t" + str(timeit.timeit(ParallelTwo, number = 1)))
    print(str(len(T2)) + "\t" + str(len(P)) + "\t" + str(timeit.timeit(SequentialThree, number = 1)) + "\t" + str(timeit.timeit(ParallelThree, number = 1)))
    print(str(len(T2)) + "\t" + str(len(P3)) + "\t" + str(timeit.timeit(SequentialFour, number = 1)) + "\t" + str(timeit.timeit(ParallelFour, number = 1)))
    print(str(len(T3)) + "\t" + str(len(P)) + "\t" + str(timeit.timeit(SequentialFive, number = 1)) + "\t" + str(timeit.timeit(ParallelFive, number = 1)))
    print(str(len(T3)) + "\t" + str(len(P4)) + "\t" + str(timeit.timeit(SequentialSix, number = 1)) + "\t" + str(timeit.timeit(ParallelSix, number = 1)))
    print(str(len(T4)) + "\t" + str(len(P)) + "\t" + str(timeit.timeit(SequentialSeven, number = 1)) + "\t" + str(timeit.timeit(ParallelSeven, number = 1)))
    print(str(len(T4)) + "\t" + str(len(P5)) + "\t" + str(timeit.timeit(SequentialEight, number = 1)) + "\t" + str(timeit.timeit(ParallelEight, number = 1)))
    print(str(len(T5)) + "\t" + str(len(P)) + "\t" + str(timeit.timeit(SequentialNine, number = 1)) + "\t" + str(timeit.timeit(ParallelNine, number = 1)))
    print(str(len(T5)) + "\t" + str(len(P6)) + "\t" + str(timeit.timeit(SequentialTen, number = 1)) + "\t" + str(timeit.timeit(ParallelTen, number = 1)))
    print(str(len(T6)) + "\t" + str(len(P)) + "\t" + str(timeit.timeit(SequentialEleven, number = 1)) + "\t" + str(timeit.timeit(ParallelEleven, number = 1)))
    print(str(len(T6)) + "\t" + str(len(P7)) + "\t" + str(timeit.timeit(SequentialTwelve, number = 1)) + "\t" + str(timeit.timeit(ParallelTwelve, number = 1)))
    #pass

def print_results(L) :
    """Prints the list of indices for the matches."""
    print("Starting Indices of Matches " + str(L))
    #pass

def naive_string_matcher(T, P) :
    """Naive string matcher algorithm from textbook page 988.

    Slight variation of the naive string matcher algorithm from
    textbook page 988.  Specifically, the textbook version prints the
    results.  This python function does not print the results.
    Instead, it generates and returns a list of the indices at the start
    of each match.  For example, if T="abcabcabc" and P="def", this function
    will return the empty list [] since the pattern doesn't appear in T.
    For that same T, if the pattern P="abc", then this function will return
    the list [0, 3, 6] since the pattern appears 3 times, beginning on indices
    0, 3, and 6.

    Keyword arguments:
    T -- the text string to search for patterns.
    P -- the pattern string.
    """
    n = len(T)
    m = len(P)
    L = []
    for s in range(n - m + 1):
        if P == T[s:s+m]:
            L.append(s)
    return L


def p_naive_string_matcher(T, P) :
    """Parallel naive string matcher algorithm from Problem Set 4.

    This function implements the parallel naive string matcher algorithm that you specified in
    Problem Set 4.  You may assume in your implementation that there are 4 processor cores.
    If you want to write this more generally, you may add a parameter to the function for number
    of processes.  If you do, don't change the order of the existing parameters, and your new parameters
    must follow, and must have default values such that if the only parameters I pass are T and P, that
    you default to 4 processes.

    Like the sequential implementation from step 1 of assignment, this function should not
    print results.  Instead, have it return a list of the indices where the matches begin.
    For example, if T="abcabcabc" and P="def", this function
    will return the empty list [] since the pattern doesn't appear in T.
    For that same T, if the pattern P="abc", then this function will return
    the list [0, 3, 6] since the pattern appears 3 times, beginning on indices
    0, 3, and 6.

    You must use Process objects (or a Pool of processes) from the multiprocessing module and not Threads from threading because
    in the next step of the assignment, you're going to investigate performance relative to the sequential
    implementation.  And due to Python's global interpreter lock, you won't see any gain if you use threads.

    You will need to decide how to distribute the work among the processes.
    One way (not the only way) is to give all of your processes T and P, and to give each process
    a range of starting indices to check, such that you give each approximately equal sized ranges.
    Another way is to give all processes the pattern string P, but only a substring of T (of approximately
    equal size).  In this case, you'd need to figure out how to map the indices back into the original.

    You will need to decide how to get the results back from the processes.
    One way (not the only way) is to give all processes a reference to a Queue object for the results.

    If you give all processes the full T and P, then if the size of the text T is large, the savings from
    multiprocessing may be outweighed by the cost of giving each its own independent copy of T.
    You might try using an Array object to use shared memory.  Here's how to do it.  Create an array of
    characters in shared memory with: a = Array(ctypes.c_wchar, "Hello World", lock=None)
    You'll need to import ctypes
    for this to work.  You can then access individual characters with a[0], a[1], etc.
    You might do this for both T and P.  None of the processes need to change them, so there is no risk
    of a race condition.

    An alternative to using Process objects directly is to use a Pool, and in particular to use the Pool.map
    method.  Hints to help you if you want to consider this approach: 1) You'll need a function of one argument
    to pass to Pool.map, and a list of the values for that argument.  This list can be a list of the starting indices
    to check for matches (i.e., the indices from the outer loop of the naive string matcher).  The one argument function's
    one argument can be the index to check, and can then check if a match starts at that index. 2) But wait, wouldn't that
    function need 3 arguments, T, P, and the index? Yes. Start by creating a helper function with those 3 arguments, with
    index as the last argument.  Your helper can simply return a boolean indicating whether it is a match.
    Then, look up the documentation for a function named partial in the Python module functools.
    partial takes as arguments a function and some of the arguments for it, and returns to you a function where those arguments
    will be passed by default.  E.g., you can pass your helper function, and T and P to partial, and it will return to you a
    function that you simply need to pass index (the remaining argument).  3) Your last hint.  If you follow hints 1 and 2, you'll
    end up with a list of booleans, true if that corresponding index was a match and false otherwise.  The fibnal step would
    be to use that to generate what this string matcher is actually supposed to return.

    Keyword arguments:
    T -- the text string to search for patterns.
    P -- the pattern string.
    """
    n = len(T)
    m = len(P)
    L = [x for x in range(n - m + 1)]
    thread = partial(isMatch, r = T, p = P)
    with Pool(4) as pool:
        L_pool = list(pool.map(thread, L))
    V = []
    for i in range(len(L_pool)):
        if(L_pool[i] == True):
            V.append(i)
    return V
    #pass

def isMatch(index, r, p) :
    if p == r[index:index+len(p)]:
        return True
    return False

if __name__ == "__main__":
    time_results()