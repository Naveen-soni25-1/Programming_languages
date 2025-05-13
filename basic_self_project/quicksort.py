def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
my_list = [10, 33, 12, 13, 17, 14, 21, 30 ,45, 34, 96, 45, 7, 8, 67, 50, 67]

print(quicksort(my_list))