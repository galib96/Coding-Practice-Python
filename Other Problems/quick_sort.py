def quicksort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)

        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
   
    else:
        return array


arr = [12,4,5,6,7,3,1,7,15,12,4,5,6,7,3,1,7,15]

print(quicksort(arr))