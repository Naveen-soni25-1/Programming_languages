def binary_search(arr, input_value):
    low = 0
    high = len(arr) - 1
#while loop is used to continue the process untill the value is find
    while low <= high:
        mid = (low + high) // 2 
        guess = arr[mid]

        if guess == input_value:
            return mid
        elif guess > input_value:
           high = mid - 1 
        else:
            low = mid + 1 

    return None 
#give position of the input_value  in the form of index
my_list = [value for value in range(1,101)]
result = binary_search(my_list, 51)
print(result)  
