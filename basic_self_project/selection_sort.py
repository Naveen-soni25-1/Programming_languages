#list that needed to sort 
my_list = [12,35,68,34,100,145,246,1726]

def find_smallest(arr):
    #find smallest no. and return it
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    # return a sorted list
    new_arr = []
    smallest = find_smallest(arr)
    new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort(my_list))