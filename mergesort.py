# Implement mergesort.

# Mergesort works by dividing the list into one-element sections, then
# comparing each pair of elements and "merging" them together in the correct
# sequence. It keeps doing this merging until the list is restored.

def merge(a1, a2):
    masterlist = []
    while True:
        if len(a1) == 0:
            masterlist += a2
            return masterlist
        elif len(a2) == 0:
            masterlist += a1
            return masterlist

        # Now to merge them...
        masterlist.append(min(a1[0], a2[0]))

        # Delete from original list
        if a1[0] < a2[0]:
            del a1[0]
        elif a1[0] > a2[0]:
            del a2[0]
        else:   # They were equal
            masterlist.append(a1[0])
            del a1[0]
            del a2[0]

def mergesort(array):
    if len(array) <= 1:
        return array

    # Divide the list in half. 
    half = len(array) // 2
    a1 = mergesort(array[:half])
    a2 = mergesort(array[half:])
    return merge(a1, a2)
    
