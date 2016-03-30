# Implement in-place quicksort.
from random import *

# Quicksort works by picking a pivot point and partitioning the list s.t.
# elements to the left are less than the pivot and vice versa for larger
# elements. Recursively do this partitioning until the array is sorted.
# Time complexity: O(n log n) best/avg case, O(n^2) worst case.
# Space complexity: O(n) worst case (naive), O(log n) best case

# Helper function for partitioning. Returns the pivot's index after
# paritioning. We do everything in place. 
def partition(array, start, end, pivot_ind):
    # Partition the array into 3 parts: elements < the pivot, the pivot,
    # and elements >= the pivot.
    # Let's first move the pivot to the first element in the list by swapping
    # it with the element at the start.
    array[start], array[pivot_ind] = array[pivot_ind], array[start]
    pivot_ind = start

    # We're going to go through the list and do the following:
    #   If the element >= pivot, it belongs in the right partition. 
    #   If the element < pivot, it belongs in the left partition.
    # We need to keep track of the first index of the right partition.
    right = start + 1

    for i in range(start + 1, end + 1):
        if array[i] < array[pivot_ind]:
            # Element belongs in left partition. Swap the first element of
            # the right partition with this element. Then the index of the
            # first element of the right partition goes up by one. 
            array[i], array[right] = array[right], array[i]
            right += 1
        i += 1
        print(right)
    # Finally, we put the pivot in its place.
    array[pivot_ind], array[right - 1] = array[right - 1], array[pivot_ind]
    pivot_ind = right - 1
    return pivot_ind

def quicksort(array, start=0, end=None):
    # start and end are the indices of the first and last elements to be sorted
    if len(array) <= 1:  # Empty or single element array
        return
    if end is None:             # Get index of last element if not given
        end = len(array) - 1
    if end - start < 1:         # Starting index is greater than ending index
        return
    
    # We will randomly choose a pivot point. (This reduces the chance
    # that we get worst case time complexity if the list is already
    # sorted, which is what happens if we choose first or last element.
    # Although, we can still get worst case complexity if the two
    # parts are poorly split.)
    pivot = randint(start, end)

    # Now we'll run the parition function recursively.
    pivot = partition(array, start, end, pivot)
    quicksort(array, start, pivot - 1)
    quicksort(array, pivot + 1, end)
